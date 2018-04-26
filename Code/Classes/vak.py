"""
Bestand met Vak klasse en lijsten Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class Vak(object):
    """
    Klasse om een vak te representeren
    """
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

    def __repr__(self):
        return self.naam


    def studentenSplitsen(self, aantalStudenten, maximaal, studenten):
        """ Split de studenten in meerdere colleges."""

        # om studenten per werkcollege in op te slaan
        werkcolleges = []

        # berekenen hoeveel werkcolleges er moeten worden gegeven
        aantalWc = math.ceil(aantalStudenten / maximaal)
        studPerWc = math.ceil(aantalStudenten / aantalWc)

        for i in range(0, aantalStudenten, studPerWc):
            werkcolleges.append(studenten[i: i + studPerWc])

        return werkcolleges


    def vanVakNaarActiviteit(self):
        # vakken omzetten naar activiteiten
        import activiteit as ActiviteitKlasse
        activiteitenLijst = []
        # hoorcollege naar activiteiten
        if self.hc > 0:
            i = self.hc
            while(i != 0):
                activiteitenLijst.append(ActiviteitKlasse.Activiteit(i, 0, self.id, 1000, self.aantalStudenten, self.studenten))
                i -= 1

        # werkcollege naar activiteiten
        if self.maxWc < self.aantalStudenten and self.wc > 0:
            studPerWc = studentenSplitsen(self.aantalStudenten, self.maxWc, self.studenten)
            i = 1
            for stud in studPerWc:
                activiteitenLijst.append(ActiviteitKlasse.Activiteit(i, 1, self.id, self.maxWc,len(stud), stud))
                i += 1
        elif self.wc > 0:
            activiteitenLijst.append(ActiviteitKlasse.Activiteit(1, 1, self.id, self.maxWc, self.aantalStudenten, self.studenten))

        # practicum naar activiteiten
        if self.maxPrac < self.aantalStudenten and self.prac > 0:
            studPerPrac = studentenSplitsen(self.aantalStudenten, self.maxPrac, self.studenten)
            i = 1
            for stud in studPerPrac:
                activiteitenLijst.append(ActiviteitKlasse.Activiteit(i, 2, self.id, self.maxPrac,len(stud), stud))
                i += 1
        elif self.prac > 0:
            activiteitenLijst.append(ActiviteitKlasse.Activiteit(1, 2, self.id, self.maxPrac, self.aantalStudenten, self.studenten))

        return activiteitenLijst
