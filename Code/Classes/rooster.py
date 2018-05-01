"""
Rooster klasse

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import csv

import student as StudentKlasse
import vak as VakKlasse
import zaalSlot as ZaalSlotKlasse


class Rooster(object):
    """ Klasse om een rooster te representeren."""
    def __init__(self, lesdagen, tijdsloten):
        self.studentenLijst = []
        self.vakkenLijst = []
        self.activiteitenLijst = []
        self.zaalslotenLijst = []
        self.idNaarTijdslot = {}
        self.vanVakNaarId = {}
        self.lesdagen = lesdagen
        self.dagNaarId = {}
        self.idNaarDag = {}
        zetTijdslotenOmNaarID(self, tijdsloten)
        zetDagOmNaarId(self, lesdagen)
        maakVakken(self)
        maakStudenten(self)
        maakZaalsloten(self)
        maakActiviteiten(self)


    def vulRandom(self):
        "Vult het rooster met activiteiten"
        i = 0
        # plaatst elk activiteit in het eerste beschikbare zaalslot
        for zaalslot in self.zaalslotenLijst:
            if len(self.activiteitenLijst) == i:
                break
            else:
                zaalslot.voegToe(self.activiteitenLijst[i])
                i += 1


    def score(self):
        "deze functie berekent de score van een rooster"

        # maakt een rooster structuur van de activiteitenlijst
        rooster = maakRooster(self)

        # berekent de malus- en bonuspunten per onderdeel
        if vakkenIngeroosterd(self):
            malusPunten = vakSpreiding(self) + zaalgrootteConflict(self) + roosterConflicten(self, rooster)  + extraTijdslot(self)
            scorepunten = 1000 - malusPunten
            print("vakspreiding: " + str(vakSpreiding(self)))
            print("zaalgrootteConflict: " + str(zaalgrootteConflict(self)))
            print("roosterConflicten: " + str(roosterConflicten(self, rooster)))
            print("extra tijdslot: " + str(extraTijdslot(self)))
            return "score rooster: " + str(scorepunten)
        else:
            return "niet alle vakken zijn ingeroosterd, geen score"

def vakkenIngeroosterd(self):
    """ Controleert of alle vakken zijn ingeroosterd."""

    # controleert of een activiteit nog niet is ingeroosterd aan de had van tijdslot 0
    for activiteit in self.activiteitenLijst:
        if activiteit.tijdslot == 0:
            return False
    return True

def extraTijdslot(self):
    "deze functie berekent de punten bij het gebruik van het extra tijdslot"

    malusPunten = 0

    # kijkt of zaal in tijdslot 5 (17.00-19.00) wordt gebruikt
    for zaal in self.zaalslotenLijst:
        if zaal.tijdslot == 5 and zaal.inGebruik == 1:
            malusPunten += 50

    return malusPunten

def vakSpreiding(self):
    "deze functie berekent de punten voor de spreiding van de activiteiten"

    malusPunten = 0



    # kijkt voor elk vak
    for vak in self.vakkenLijst:
        verdeeldAantalDagen = 0
        dag = []
        for activiteit in self.activiteitenLijst:
            if activiteit.vakId == vak.id:
                if activiteit.dag not in dag:
                    dag.append(activiteit.dag)
                    verdeeldAantalDagen += 1

        aantalActiviteiten = vak.hc + vak.wc + vak.prac

        x = aantalActiviteiten - verdeeldAantalDagen

        malusPunten = malusPunten + x * 10

    return malusPunten


def maakRooster(self):
    rooster = []
    for i in range(len(self.lesdagen) + 1):
        rooster.append([])
        for j in range(len(self.idNaarTijdslot) + 1):
            rooster[i].append([])

    for zaalslot in self.zaalslotenLijst:
        i = int(zaalslot.dag)
        j = int(zaalslot.tijdslot)
        rooster[i][j].append(zaalslot)

    return rooster


def roosterConflicten(self, rooster):
    "deze functie berekent de punten bij roosterconflicten per student"

    malusPunten = 0

    for dag in rooster:
        for tijdslot in dag:
            studentenTijdslot = []
            for zaalslot in tijdslot:
                if zaalslot.activiteit != None:
                    studentenTijdslot += zaalslot.activiteit.welkeStud
            malusPunten += controleerDubbel(studentenTijdslot)
    return malusPunten

def controleerDubbel(studentenTijdslot):
    malusPunten = 0
    aanwezig = []
    for student in studentenTijdslot:
        if student in aanwezig:
            malusPunten += 1
        else:
            aanwezig.append(student)
    return malusPunten

def zalenInGebruik(self):
    zalenGebruikt = []
    for zaalslot in self.zaalslotenLijst:
        if zaalslot.inGebruik == 1:
            zalenGebruikt.append(zaalslot)
    return zalenGebruikt

def zaalgrootteConflict(self):
    "deze functie berekent de maluspunten voor te kleine zalen"
    zalenGebruikt = zalenInGebruik(self)
    malusPunten = 0
    for zaalslot in zalenGebruikt:
        verschil = zaalslot.capaciteit - zaalslot.activiteit.nrStud
        if verschil < 0:
            malusPunten = malusPunten + abs(verschil)
    return malusPunten

def zetDagOmNaarId(self, lesdagen):
    for i in range(1, len(lesdagen) + 1):
        self.dagNaarId[lesdagen[i - 1]] = i
        self.idNaarDag[i] = lesdagen[i - 1]

def zetTijdslotenOmNaarID(self, tijdsloten):
    for i in range(1, len(tijdsloten) + 1):
        self.idNaarTijdslot[i] = tijdsloten[i - 1]

def maakVakken(self):
    """ Leest het csv bestand in en maakt een vakkenlijst."""
    # aanmaken van verschillende functies
    teller = 0

    # inlezen van CSV bestand van vakken
    with open('Data/vakken.csv') as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=';')
        next(leesCSV, None)

        # rijen van CSV inlezen en vakobject aanmaken
        for rij in leesCSV:
            # nvt naar "oneindig zetten"
            if rij[3] == "nvt":
                rij[3] = 1000
            if rij[5] == "nvt":
                rij[5] = 1000

            self.vakkenLijst.append(VakKlasse.Vak(teller, rij[0], int(rij[1]), int(rij[2]), int(rij[3]), int(rij[4]), int(rij[5])))
            self.vanVakNaarId[rij[0]] = teller
            teller += 1

def maakStudenten(self):
    """ Leest het csv bestand in en maakt een studentenlijst."""
    # inlezen van CSV bestand van studenten
    with open("Data/studentenenvakken.csv", "r", encoding="latin-1") as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=",")
        next(leesCSV, None)

        # leest bestand en creeert studenten
        for rij in leesCSV:
            studentVakken = []
            for vak in rij[3:]:
                if vak != "":
                    studentVakken.append(vak)
            self.studentenLijst.append(StudentKlasse.Student(rij[0], rij[1], rij[2], studentVakken))

    # vakken in studentenlijst met id voorzien
    for student in self.studentenLijst:
        tijdelijk = []
        for vak in student.vakken:
            tijdelijk.append(self.vanVakNaarId[vak])
        student.vakken = tijdelijk

    # aantal studenten per vak vastleggen
    for vak in self.vakkenLijst:
        for student in self.studentenLijst:
            if vak.id in student.vakken:
                vak.studenten.append(student.studentnummer)
        vak.aantalStudenten = len(vak.studenten)


def maakZaalsloten(self):

    # leest bestand en creert zaalsloten
    with open("Data/zalen.csv") as csvBestand:
        leesCSV = csv.reader(csvBestand, delimiter=';')
        next(leesCSV, None)
        # leest elke zaal en maakt per dag en tijdslot een zaalslot
        for rij in leesCSV:
            for dag in self.lesdagen:
                for i in range(1, len(self.idNaarTijdslot)):
                    self.zaalslotenLijst.append(ZaalSlotKlasse.ZaalSlot(rij[0], int(rij[1]), self.dagNaarId[dag], i, self.idNaarDag))

        # voeg zaalsloten toe voor het laatste tijdslot 17.00-19.00
        for dag in self.lesdagen:
            self.zaalslotenLijst.append(ZaalSlotKlasse.ZaalSlot("C0.110", 110, self.dagNaarId[dag], 5, self.idNaarDag))

def maakActiviteiten(self):
    for vak in self.vakkenLijst:
        self.activiteitenLijst += vak.vanVakNaarActiviteit()
