import csv

class Student(object):
    def __init__(self, achternaam, voornaam, studentnummer, vakken):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.studentnummer = studentnummer
        self.vakken = vakken

studentenLijst = []

with open('studentenenvakken.csv', 'r', encoding="latin-1") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        studentVakken = []
        for vak in row[3:]:
            if vak != "":
                studentVakken.append(vak) 
        studentenLijst.append(Student(row[0], row[1], row[2], studentVakken))

# discard first row with Excel variable names
studentenLijst = studentenLijst[1:]

csvfile.close()
