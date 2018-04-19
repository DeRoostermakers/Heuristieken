"""
Hoofdbestand Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""
import csv
import math
import student as StudentKlasse
import activiteit as ActiviteitKlasse
import zaal as ZaalKlasse
import vak as VakKlasse
import copy

# initialiseer lijsten met data
studentenLijst = []
vakkenLijst = []
zaalLijst = []
vanVakNaarId = {}
inTeRoosteren = []

def main():

    initialize()

    # dict om id van tijdsloten om te zetten naar tijd
    idNaarTijdslot = {1 : "9:00-11:00", 2 : "11:00-13:00", 3 : "13:00-15:00", 4 : "15:00-17:00"}

    # dict met alle zalen per dag
    dag = {1 : zaalLijst[:], 2 : zaalLijst[:], 3 : zaalLijst[:], 4 : zaalLijst[:]}

    # weekrooster met tijdslots en zalen
    rooster = {"maandag" : copy.deepcopy(dag), "dinsdag" : copy.deepcopy(dag), "woensdag" : copy.deepcopy(dag), "donderdag" : copy.deepcopy(dag), "vrijdag" : copy.deepcopy(dag)}

def initialize():

    # aanmaken van dict en vakkenlijst creëren
    counter = 0

    # inlezen van CSV bestand
    with open('vakken.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=';')
        next(readCSV, None)

        # rijen van CSV inlezen en vakobject aanmaken
        for row in readCSV:
            # verander nvt naar "oneindig"
            if row[3] == "nvt":
                row[3] = 1000
            if row[5] == "nvt":
                row[5] = 1000

            vakkenLijst.append(VakKlasse.Vak(counter, row[0], row[1], row[2], int(row[3]), row[4], int(row[5])))
            vanVakNaarId[row[0]] = counter
            counter += 1

    # inlezen van CSV bestand
    with open('studentenenvakken.csv', 'r', encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None)
        for row in reader:
            studentVakken = []
            for college in row[3:]:
                if college != "":
                    studentVakken.append(college)
            studentenLijst.append(StudentKlasse.Student(row[0], row[1], row[2], studentVakken))

    # vakken in studentenlijst met id voorzien
    for student in studentenLijst:
        temp = []
        for vak in student.vakken:
            temp.append(vanVakNaarId[vak])
        student.vakken = temp

    # aantal studenten per vak vastleggen
    for vak in vakkenLijst:
        for student in studentenLijst:
            if vak.id in student.vakken:
                vak.studenten.append(student.studentnummer)
        vak.aantalStudenten = len(vak.studenten)

    with open('zalen.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=';')
        next(readCSV, None)
        for row in readCSV:
            zaalLijst.append(ZaalKlasse.Zaal(row[0], row[1], 0, 0))

    # vakken omzetten naar activiteiten
    for vak in vakkenLijst:

        # werkcollege naar activiteiten
        if vak.maxWc < vak.aantalStudenten:
            studPerWc = studentenSplitsen(vak.aantalStudenten, vak.maxWc, vak.studenten)
            i = 1
            for stud in studPerWc:
                inTeRoosteren.append(ActiviteitKlasse.Activiteit(i, 1, vak.id, vak.maxWc,len(stud), stud))
                i += 1
        else:
            inTeRoosteren.append(ActiviteitKlasse.Activiteit(1, 1, vak.id, vak.maxWc, vak.aantalStudenten, vak.studenten))


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
