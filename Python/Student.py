import csv

class Student(object):
    def __init__(self, achternaam, voornaam, studentnummer):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.studentnummer = studentnummer
        self.vakken = []

with open('studentenenvakken.csv', 'rb', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        print(row)

csvfile.close()
