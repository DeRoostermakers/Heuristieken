"""
Bestand met Student klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import csv
import vak as vakClass

class Student(object):
    """
    Klasse om een student te representeren
    """
    def __init__(self, achternaam, voornaam, studentnummer, vakken):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.studentnummer = studentnummer
        self.vakken = vakken

    def __str__(self):
        return self.studentnummer

    def __repr__(self):
        return self.studentnummer

# initialiseer lijsten voor vakken en studenten
studentenLijst = []
vakkenLijst = vakClass.vakkenLijst

# inlezen van CSV bestand
with open('studentenenvakken.csv', 'r', encoding="latin-1") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        studentVakken = []
        for college in row[3:]:
            if college != "":
                studentVakken.append(college)
        studentenLijst.append(Student(row[0], row[1], row[2], studentVakken))
csvfile.close()

# eerste regel met variabelenamen verwerpen
studentenLijst = studentenLijst[1:]

# vakken in studentenlijst met id voorzien
for student in studentenLijst:
    temp = []
    for vak in student.vakken:
        temp.append(vakClass.vanVakNaarId[vak])
    student.vakken = temp

# aantal studenten per vak vastleggen
for vak in vakkenLijst:
    for student in studentenLijst:
        if vak.id in student.vakken:
            vak.studenten.append(student.studentnummer)
    vak.aantalStudenten = len(vak.studenten)
