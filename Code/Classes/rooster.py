"""
Rooster klasse

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import csv
import random
# import numpy
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
        self.vanIdNaarVak = {}
        self.lesdagen = lesdagen
        self.dagNaarId = {}
        self.idNaarDag = {}
        self.zetIdOmNaarTijdslot(tijdsloten)
        self.zetDagOmNaarId(lesdagen)
        self.maakVakken()
        self.maakStudenten()
        self.maakZaalsloten()
        self.maakActiviteiten()


    def vulRandom(self):
        "Vult het rooster met activiteiten"
        i = 0
        j = 0
        randomIndexActiviteiten = random.sample(range(len(self.activiteitenLijst)),
                                    len(self.activiteitenLijst))
        randomIndexSloten = random.sample(range(len(self.zaalslotenLijst)),
                                    len(self.zaalslotenLijst))

        # plaatst elk activiteit in het een willekeurig zaalslot
        for zaalslot in range(0, len(self.activiteitenLijst)):
            self.zaalslotenLijst[randomIndexSloten[j]].voegToe(self.activiteitenLijst[randomIndexActiviteiten[i]])
            i += 1
            j += 1

    def score(self):
        "deze functie berekent de score van een rooster"

        # maakt een rooster structuur van de activiteitenlijst
        perGroep = self.weekIndeling()

        # berekent de malus- en bonuspunten per onderdeel
        if self.vakkenIngeroosterd():
            bonusPunten = self.bonus(perGroep)
            vakSpreidingPunten = self.vakSpreiding(perGroep)
            zaalgrootteConflictPunten = self.zaalgrootteConflict()
            roosterConflictenPunten = self.roosterConflicten()
            extraTijdslotPunten = self.extraTijdslot()
            malusPunten = vakSpreidingPunten + zaalgrootteConflictPunten + roosterConflictenPunten + extraTijdslotPunten

            scorepunten = 1000 - malusPunten + bonusPunten
            print("vakspreiding: " + str(vakSpreidingPunten))
            print("zaalgrootteConflict: " + str(zaalgrootteConflictPunten))
            print("roosterConflicten: " + str(roosterConflictenPunten))
            print("extra tijdslot: " + str(extraTijdslotPunten))
            print("bonuspunten: " + str(bonusPunten))
            print("score: " + str(scorepunten))
            return scorepunten

        else:
            return "niet alle vakken zijn ingeroosterd, geen score"

    def zetIdOmNaarTijdslot(self, tijdsloten):
        "Maakt een dict om een id om te zetten naar een tijdslot."
        for i in range(1, len(tijdsloten) + 1):
            self.idNaarTijdslot[i] = tijdsloten[i - 1]

    def zetDagOmNaarId(self, lesdagen):
        "Maakt een dict om dagen om te zetten naar een id."
        for i in range(1, len(lesdagen) + 1):
            self.dagNaarId[lesdagen[i - 1]] = i
            self.idNaarDag[i] = lesdagen[i - 1]

    def maakVakken(self):
        "Leest het csv bestand in en maakt een vakkenlijst."
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
                self.vanIdNaarVak[teller] = rij[0]
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
                self.studentenLijst.append(StudentKlasse.Student(rij[0], rij[1], int(rij[2]), studentVakken))

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
        "Maakt een lijst met zaalsloten aan."

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
        "Zet de vakkenlijst om naar een activiteitenlijst."
        for vak in self.vakkenLijst:
            self.activiteitenLijst += vak.vanVakNaarActiviteit()

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

    def vakSpreiding(self, perGroep):
        "deze functie berekent de punten voor de spreiding van de activiteiten"
        malusPunten = 0

        # controleer per vakgroep de vakspreiding door de week
        for groep in perGroep:
            dagGeweest = []
            # controleer of op de dag al een activiteit is geweest
            for dag in groep:
                if dag in dagGeweest:
                    malusPunten += 10
                else:
                    dagGeweest.append(dag)
        return malusPunten

    def zaalgrootteConflict(self):
        "Deze functie berekent de maluspunten voor te kleine zalen"
        # vraagt alle zaalsloten op welke worden gebruikt
        malusPunten = 0

        # kijkt of de capaciteit van de zaal te klein is voor het aantal studenten
        for zaalslot in self.zaalslotenLijst:
            if zaalslot.inGebruik == 1:
                verschil = zaalslot.capaciteit - zaalslot.activiteit.nrStud
                # berekent het aantal maluspunten als zaal te klein is
                if verschil < 0:
                    malusPunten = malusPunten + abs(verschil)
        return malusPunten

    def maakRooster(self):
        "Maakt een rooster structuur met lijsten en voeg de zaalsloten toe"
        rooster = []

        # maak het aantal lijsten voor het aantal dagen, gebruik het id als index
        for i in range(len(self.lesdagen) + 1):
            rooster.append([])
            # maak het aantal lijsten voor het aantal tijdsloten, gebruik het id als index
            for j in range(len(self.idNaarTijdslot) + 1):
                rooster[i].append([])

        # voeg het zaalslot toe op de juiste plaats in het rooster
        for zaalslot in self.zaalslotenLijst:
            i = int(zaalslot.dag)
            j = int(zaalslot.tijdslot)
            rooster[i][j].append(zaalslot)

        return rooster


    def weekIndeling(self):
        "Maakt per werkgroep een lijst aan met de activiteiten door de week"
        perGroep = []
        # per vak kijken naar de spreiding
        for vak in self.vakkenLijst:
            hcDag = []
            wcDag = []
            pracDag = []
            # kijk naar alle activiteiten binnen een vak
            for activiteit in self.activiteitenLijst:
                if vak.id == activiteit.vakId:
                    if activiteit.soort == 0:
                        hcDag.append(activiteit.dag)
                    if activiteit.soort == 1:
                        wcDag.append(activiteit.dag)
                    if activiteit.soort == 2:
                        pracDag.append(activiteit.dag)

            # voor alle mogelijke splitsingen een weeklijst maken
            for i in range(max(len(wcDag),len(hcDag),len(pracDag))):
                lijst =[]

                # voeg alle hoorcolleges toe
                lijst.extend(hcDag)

                # voeg de werkgroep toe van splitsing i
                if len(wcDag) > 0:
                    lijst.append(wcDag[i])

                # voeg de werkgroep toe van splitsing i
                if len(pracDag) > 0:
                    lijst.append(pracDag[i])

                perGroep.append(lijst)

        return perGroep

    def bonus(self, perGroep):
        "Berekent de bonuspunten van de vakspreiding"
        bonus = 0

        # kijkt per werkgroep (vanuti student) of de verdeling van de activiteiten goed is
        for groep in perGroep:
            groep.sort()
            # twee activiteiten: dan moeten er twee dagen tussen de activiteiten zitten
            if len(groep) == 2:
                if groep[1] - groep[0] == 3:
                    bonus += 20
            # drie activiteiten: moeten er twee dagen tussen alle drie de activiteiten zitten
            if len(groep) == 3:
                if groep[1] - groep[0] == 2 and groep[2] - groep[1] == 2:
                    bonus += 20
            # vier activiteiten: eerste twee, en laatste twee moet een dag tussen zitten
            if len(groep) == 4:
                if groep[1] - groep[0] == 1 and groep[2] - groep[1] == 2 and groep[3] - groep[2] == 1:
                    bonus += 20

        return bonus



    def roosterConflicten(self):
        "deze functie berekent de punten bij roosterconflicten per student"

        malusPunten = 0
        rooster = self.maakRooster()
        # kijk voor elke dag naar een tijdslot
        for dag in rooster:
            # kijk voor elk tijdslot welke studenten een vak volgen
            for tijdslot in dag:
                studentenTijdslot = []
                # voeg alle studenten samen in een lijst
                for zaalslot in tijdslot:
                    if zaalslot.activiteit != None:
                        studentenTijdslot += zaalslot.activiteit.welkeStud
                #  bereken de maluspunten voor de rooster conflicten
                malusPunten += controleerDubbel(studentenTijdslot)
        return malusPunten

def controleerDubbel(studentenTijdslot):
    "Controleert hoeveel rooster conflicten een bepaald tijdslot heeft"
    malusPunten = 0
    aanwezig = []

    # kijkt of een student al aanwezig was in het tijdslot
    for student in studentenTijdslot:
        if student in aanwezig:
            malusPunten += 1
        else:
            aanwezig.append(student)
    return malusPunten
