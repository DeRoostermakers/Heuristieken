import csv

vakkenlijst = []

with open('vakken.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=';')
    print(readCSV)




    class Vak(object):
        """docstring for [object Object]."""
        def __init__(self, id, naam, hc, wc, maxWc, prac, maxPrac):
            self.id = id
            self.naam = naam
            self.hc = hc
            self.wc =  wc
            self.maxWc = maxWc
            self.prac = prac
            self.maxPrac = maxPrac
            self.aantalStudenten = 0
            self.studenten = []

        def __str__(self):
            return self.naam

    for row in readCSV:
        vakkenlijst.append(Vak(1, row[0], row[1], row[2], row[3], row[4], row[5]))

    for vak in vakkenlijst:
        print(vak)
