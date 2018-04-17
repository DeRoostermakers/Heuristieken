import csv

with open('vakken.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=';')

    for row in readCSV:
        print(row)


class Vak(object):
    """docstring for [object Object]."""
    def __init__(self, id, naam, hc, wc, maxWc, prac, maxPrac, aantalStudenten):
        self.id = id
        self.naam = naam
        self.hc = hc
        self.wc =  wc
        self.maxWc = maxWc
        self.prac = prac
        self.maxPrac = maxPrac
        self.aantalStudenten = aantalStudenten
        self.studenten = []
