"""
Bestand met functie die de maluspunten voor de roosterconflicten berekent

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

def roosterconflicten(studentenLijst, zaalslotLijst):
    "deze functie berekent de punten bij roosterconflicten per student"

    malusPunten = 0

    for student in studentenLijst:
        tijslotenStudent = []

        for zaalslot in zaalslotLijst:
            if student in zaalslot.activiteit.welkeStud:
                dagtijd = [zaalslot.dag, zaalslot.tijdslot]
                if dagtijd not in tijdslotenStudent:
                    tijdslotenStudent.append(dagtijd)
                else:
                    malusPunten += 1

    return malusPunten
