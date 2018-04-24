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
        for rij in leesCSV:
            zaalLijst.append(ZaalKlasse.Zaal(rij[0], rij[1], 0, 0))


    # vakken omzetten naar activiteiten
    for vak in vakkenLijst:
        # hoorcollege naar activiteiten
        if vak.hc > 0:
            i = vak.hc
            while(i != 0):
                inTeRoosteren.append(ActiviteitKlasse.Activiteit(i, 0, vak.id, 1000, vak.aantalStudenten, vak.studenten))
                i -= 1

        # werkcollege naar activiteiten
        if vak.maxWc < vak.aantalStudenten and vak.wc > 0:
            studPerWc = studentenSplitsen(vak.aantalStudenten, vak.maxWc, vak.studenten)
            i = 1
            for stud in studPerWc:
                inTeRoosteren.append(ActiviteitKlasse.Activiteit(i, 1, vak.id, vak.maxWc,len(stud), stud))
                i += 1
        elif vak.wc > 0:
            inTeRoosteren.append(ActiviteitKlasse.Activiteit(1, 1, vak.id, vak.maxWc, vak.aantalStudenten, vak.studenten))


        # practicum naar activiteiten
        if vak.maxPrac < vak.aantalStudenten and vak.prac > 0:
            studPerPrac = studentenSplitsen(vak.aantalStudenten, vak.maxPrac, vak.studenten)
            i = 1
            for stud in studPerPrac:
                inTeRoosteren.append(ActiviteitKlasse.Activiteit(i, 2, vak.id, vak.maxPrac,len(stud), stud))
                i += 1
        elif vak.prac > 0:
            inTeRoosteren.append(ActiviteitKlasse.Activiteit(1, 2, vak.id, vak.maxPrac, vak.aantalStudenten, vak.studenten))


def studentenSplitsen(aantalStudenten, maximaal, studenten):
    # om studenten per werkcollege in op te slaan
    werkcolleges = []

    # berekenen hoeveel werkcolleges er moeten worden gegeven
    aantalWc = math.ceil(aantalStudenten / maximaal)
    studPerWc = math.ceil(aantalStudenten / aantalWc)

    for i in range(0, aantalStudenten, studPerWc):
        werkcolleges.append(studenten[i: i + studPerWc])

    return werkcolleges

if __name__ == "__main__":
    main()
