"""
Rooster klasse

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import csv

import student as StudentKlasse
import vak as VakKlasse
import zaalSlot as ZaalSlotKlasse



class Rooster(object):
    """ Klasse om een rooster te representeren."""
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
        maakActiviteiten(self)

    def vulRandom(self):
        i = 0
        for zaalslot in self.zaalslotenLijst:
            if len(self.activiteitenLijst) == i:
                break
            else:
                zaalslot.voegToe(self.activiteitenLijst[i])
                i += 1


    def score(self):
        "deze functie berekent de score van een rooster"

        if vakkenIngeroosterd(self):
            malusPunten = vakSpreiding(self) + zaalgrootteConflict(self) + roosterConflicten(self)  + extraTijdslot(self)
            scorepunten = 1000 - malusPunten
            print(roosterConflicten(self))
            return scorepunten
        else:
            print("Niet alle vakken ingeroosterd")
            return -1000000000

def vakkenIngeroosterd(self):
    """ Controleert of alle vakken zijn ingeroosterd."""

    # controleert of een activiteit nog niet is ingeroosterd aan de had van tijdslot 0
    for activiteit in self.activiteitenLijst:
        if activiteit.tijdslot == 0:
            print("Niet alle vakken zijn ingeroosterd")
            return False
    return True

def extraTijdslot(self):
    "deze functie berekent de punten bij het gebruik van het extra tijdslot"

    malusPunten = 0

    # kijkt of zaal in tijdslot 5 (17.00-19.00) wordt gebruikt
    for zaal in self.zaalslotenLijst:
        if zaal.tijdslot == 5 and zaal.inGebruik == 1:
            malusPunten += 50

    return malusPunten

def vakSpreiding(self):
    "deze functie berekent de punten voor de spreiding van de activiteiten"

    malusPunten = 0

    for vak in self.vakkenLijst:
        verdeeldAantalDagen = 0
        dag = []
        for activiteit in self.activiteitenLijst:
            if activiteit.vakId == vak.id:
                if activiteit.dag not in dag:
                    dag.append(activiteit.dag)
                    verdeeldAantalDagen += 1

        aantalActiviteiten = vak.hc + vak.wc + vak.prac

        x = aantalActiviteiten - verdeeldAantalDagen

        malusPunten = malusPunten + x * 10

    return malusPunten

def roosterConflicten(self):
    "deze functie berekent de punten bij roosterconflicten per student"

    malusPunten = 0
    zalenGebruikt = zalenInGebruik(self)

    for student in self.studentenLijst:
        tijdslotenStudent = []
        for zaalslot in zalenGebruikt:
            if student.studentnummer in zaalslot.activiteit.welkeStud:
                dagtijd = [zaalslot.dag, zaalslot.tijdslot]
                if dagtijd not in tijdslotenStudent:
                    tijdslotenStudent.append(dagtijd)
                else:
                    malusPunten += 1

    return malusPunten

def zalenInGebruik(self):
    zalenGebruikt = []
    for zaalslot in self.zaalslotenLijst:
        if zaalslot.inGebruik == 1:
            zalenGebruikt.append(zaalslot)
    return zalenGebruikt

def zaalgrootteConflict(self):
    "deze functie berekent de maluspunten voor te kleine zalen"
    zalenGebruikt = zalenInGebruik(self)
    malusPunten = 0
    for zaalslot in zalenGebruikt:
        verschil = zaalslot.capaciteit - zaalslot.activiteit.nrStud
        if verschil < 0:
            malusPunten = malusPunten + abs(verschil)

    return malusPunten


def zetTijdslotenOmNaarID(self, tijdsloten):
    for i in range(1, len(tijdsloten) + 1):
        self.idNaarTijdslot[i] = tijdsloten[i - 1]

def maakVakken(self):
    """ Leest het csv bestand in en maakt een vakkenlijst."""
    # aanmaken van verschillende functies
    teller = 0

    # inlezen van CSV bestand van vakken
    with open('Data/vakken.csv') as csvBestand:
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
    with open("Data/studentenenvakken.csv", "r", encoding="latin-1") as csvBestand:
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
    with open("Data/zalen.csv") as csvBestand:
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

def maakActiviteiten(self):
    for vak in self.vakkenLijst:
        self.activiteitenLijst += vak.vanVakNaarActiviteit()
