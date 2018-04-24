"""
Hoofdbestand Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))

import csv
import student as StudentKlasse
import zaal as ZaalKlasse
import vak as VakKlasse
import copy

# initialiseer lijsten met data
studentenLijst = []
vakkenLijst = []
zaalLijst = []
vanVakNaarId = {}

def main():

    initialiseer()

    # dict om id van tijdsloten om te zetten naar tijd
    idNaarTijdslot = {1 : "9:00-11:00", 2 : "11:00-13:00", 3 : "13:00-15:00", 4 : "15:00-17:00", 5 : "17:00-19:00"}

    # dict met alle zalen per dag
    dag = {1 : zaalLijst[:], 2 : zaalLijst[:], 3 : zaalLijst[:], 4 : zaalLijst[:], 5 : zaalLijst[:]}

    # weekrooster met tijdslots en zalen
    rooster = {"maandag" : copy.deepcopy(dag), "dinsdag" : copy.deepcopy(dag), "woensdag" : copy.deepcopy(dag), "donderdag" : copy.deepcopy(dag), "vrijdag" : copy.deepcopy(dag)}



def initialiseer():

    # aanmaken van dict en vakkenlijst creëren
    teller = 0

    # inlezen van CSV bestand
    with open('vakken.csv') as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=';')
        next(leesCSV, None)

        # rijen van CSV inlezen en vakobject aanmaken
        for rij in leesCSV:
            vakkenLijst.append(VakKlasse.Vak(teller, rij[0], rij[1], rij[2], rij[3], rij[4], rij[5]))
            vanVakNaarId[rij[0]] = teller
            teller += 1

    # inlezen van CSV bestand
    with open('studentenenvakken.csv', 'r', encoding="latin-1") as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=",")
        next(leesCSV, None)

        #
        for rij in leesCSV:
            studentVakken = []
            for vak in rij[3:]:
                if vak != "":
                    studentVakken.append(vak)
            studentenLijst.append(StudentKlasse.Student(rij[0], rij[1], rij[2], studentVakken))

    print("test")
    # vakken in studentenlijst met id voorzien
    for student in studentenLijst:
        tijdelijk = []
        for vak in student.vakken:
            tijdelijk.append(vanVakNaarId[vak])
        student.vakken = tijdelijk

    # aantal studenten per vak vastleggen
    for vak in vakkenLijst:
        for student in studentenLijst:
            if vak.id in student.vakken:
                vak.studenten.append(student.studentnummer)
        vak.aantalStudenten = len(vak.studenten)

    #
    with open('zalen.csv') as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=';')
        next(leesCSV, None)

        #
        for rij in leesCSV:
            zaalLijst.append(ZaalKlasse.Zaal(rij[0], rij[1], 0, 0))

if __name__ == "__main__":
    main()
