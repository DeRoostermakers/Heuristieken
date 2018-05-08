"""
Hoofd bestand om een rooster object aan te maken en algoritmes te testen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))

from hillClimber import hillClimbing
import rooster as Rooster
# from randomSteekproef import randomSteekproef

# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

# maak een rooster object aan
rooster = Rooster.Rooster(dagen, tijdsloten)

# vul het rooster met vakken
rooster.vulRandom()

hillClimbing(rooster)
# bereken de score
print(rooster.score())



# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, iteraties)


vanZaalNaarID = {"A1.04" : 0, "A1.06" : 1, "A1.08" : 2, "A1.10" : 3, "B0.201" : 4, "C0.110" : 5, "C1.112" : 6}

import csv
with open("rooster.csv", "w") as roosterCSV:
    writer = csv.writer(roosterCSV, delimiter = ';')
    writer.writerow(["RoomId", "RoomName", "Tijdslot", "Dagslot", "VakId", "Vaknaam", "Activiteit", "GroupId", "Placeholder", "Placeholder", "Studentnummers"])
    for zaalslot in rooster.zaalslotenLijst:
        if zaalslot.inGebruik != 0:
            writer.writerow([vanZaalNaarID[zaalslot.naam], zaalslot.naam, zaalslot.tijdslot - 1, zaalslot.dag - 1, zaalslot.activiteit.vakId, rooster.vanIdNaarVak[zaalslot.activiteit.vakId], zaalslot.activiteit.soort, zaalslot.activiteit.groepnr, " " , " " , zaalslot.activiteit.welkeStud])
