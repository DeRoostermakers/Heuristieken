import csv

with open('vakken.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=';')


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


    counter = -1
    vakkenlijst = []
    vanVakNaarId = {}
    for row in readCSV:
        if counter != -1:
            vakkenlijst.append(Vak(counter, row[0], row[1], row[2], row[3], row[4], row[5]))
            vanVakNaarId[row[0]] = counter
        counter += 1
    csvFile.close()
