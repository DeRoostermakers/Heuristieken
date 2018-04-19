"""
Hoofdbestand Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""
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
    
    initialize()

    # dict om id van tijdsloten om te zetten naar tijd
    idNaarTijdslot = {1 : "9:00-11:00", 2 : "11:00-13:00", 3 : "13:00-15:00", 4 : "15:00-17:00"}

    # dict met alle zalen per dag
    dag = {1 : zaalLijst[:], 2 : zaalLijst[:], 3 : zaalLijst[:], 4 : zaalLijst[:]}

    # weekrooster met tijdslots en zalen
    rooster = {"maandag" : copy.deepcopy(dag), "dinsdag" : copy.deepcopy(dag), "woensdag" : copy.deepcopy(dag), "donderdag" : copy.deepcopy(dag), "vrijdag" : copy.deepcopy(dag)}

    for dag in rooster.keys():
        print(rooster[dag][1][0])
            
    
def initialize():
    
    # aanmaken van dict en vakkenlijst creëren    
    counter = 0
    
    # inlezen van CSV bestand
    with open('vakken.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=';')
        next(readCSV, None)
    
        # rijen van CSV inlezen en vakobject aanmaken
        for row in readCSV:
            vakkenLijst.append(VakKlasse.Vak(counter, row[0], row[1], row[2], row[3], row[4], row[5]))
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

if __name__ == "__main__":
    main()
