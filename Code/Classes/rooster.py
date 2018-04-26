"""
Rooster klasse

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import os, sys
import csv

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))

import student as StudentKlasse
import vak as VakKlasse
import activiteit as ActiviteitKlasse
import zaalSlot as ZaalSlotKlasse



class Rooster(object):
    def __init__(self, lesdagen, tijdsloten):
        self.studentenLijst = []
        self.vakkenLijst = []
        self.activiteitenLijst = []
        self.zaalslotenLijst = []
        self.idNaarTijdslot = {}
        self.vanVakNaarId = {}
        self.lesdagen = lesdagen
        zetTijdslotenOmNaarID(self, tijdsloten)
        maakVakken(self)
        maakStudenten(self)
        maakZaalsloten(self)

def zetTijdslotenOmNaarID(self, tijdsloten):
    for i in range(1, len(tijdsloten) + 1):
        self.idNaarTijdslot[i] = tijdsloten[i - 1]

def maakVakken(self):
    """ Leest het csv bestand in en maakt een vakkenlijst."""
    # aanmaken van verschillende functies
    teller = 0

    # inlezen van CSV bestand van vakken
    with open("../../Data/vakken.csv") as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=';')
        next(leesCSV, None)

        # rijen van CSV inlezen en vakobject aanmaken
        for rij in leesCSV:
            # nvt naar "oneindig zetten"
            if rij[3] == "nvt":
                rij[3] = 1000
            if rij[5] == "nvt":
                rij[5] = 1000

            self.vakkenLijst.append(VakKlasse.Vak(teller, rij[0], int(rij[1]), int(rij[2]), int(rij[3]), int(rij[4]), int(rij[5])))
            self.vanVakNaarId[rij[0]] = teller
            teller += 1

def maakStudenten(self):
    """ Leest het csv bestand in en maakt een studentenlijst."""
    # inlezen van CSV bestand van studenten
    with open("../../Data/studentenenvakken.csv", "r", encoding="latin-1") as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=",")
        next(leesCSV, None)

        # leest bestand en creeert studenten
        for rij in leesCSV:
            studentVakken = []
            for vak in rij[3:]:
                if vak != "":
                    studentVakken.append(vak)
            self.studentenLijst.append(StudentKlasse.Student(rij[0], rij[1], rij[2], studentVakken))

    # vakken in studentenlijst met id voorzien
    for student in self.studentenLijst:
        tijdelijk = []
        for vak in student.vakken:
            tijdelijk.append(self.vanVakNaarId[vak])
        student.vakken = tijdelijk

    # aantal studenten per vak vastleggen
    for vak in self.vakkenLijst:
        for student in self.studentenLijst:
            if vak.id in student.vakken:
                vak.studenten.append(student.studentnummer)
        vak.aantalStudenten = len(vak.studenten)


def maakZaalsloten(self):

    # leest bestand en creert zaalsloten
    with open("../../Data/zalen.csv") as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=';')
        next(leesCSV, None)
        # leest elke zaal en maakt per dag en tijdslot een zaalslot
        for rij in leesCSV:
            for dag in self.lesdagen:
                for i in range(1, len(self.idNaarTijdslot)):
                    self.zaalslotenLijst.append(ZaalSlotKlasse.ZaalSlot(rij[0], int(rij[1]), dag, i))

        # voeg zaalsloten toe voor het laatste tijdslot 17.00-19.00
        for dag in self.lesdagen:
            self.zaalslotenLijst.append(ZaalSlotKlasse.ZaalSlot("C0.110", 110, dag, 5))
