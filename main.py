"""
Hoofd bestand om een rooster object aan te maken en algoritmes te testen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Resultaten", "Visualisatie"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))


from hillClimberStochastisch import hillClimberStochastisch
from hillClimberSteepestAscent import hillClimberSteepestAscent
from simulatedAnnealing import simulatedAnnealing
from test2 import test2
from simulatedAnnealing import simulatedAnnealing, lineairFunctie, exponentieelFunctie, sigmoidalFunctie
from eenvoudigeMinimalisatie import eenvoudigeMinimalisatie
from tweevoudigeMinimalisatie import tweevoudigeMinimalisatie
from geneticAlgorithm import geneticAlgorithm
import rooster as Rooster
from frequentieHistogram import frequentieHistogram
from iteratieVisualisatie import iteratieVisualisatie
from randomSteekproef import randomSteekproef
from visualiseer import visualiseer

# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

# roosterEnScore = hillClimber(dagen, tijdsloten)
# rooster = roosterEnScore[0]
# score = roosterEnScore[1]
<<<<<<< HEAD
# minIteraties = 100
# rooster = Rooster.Rooster(dagen, tijdsloten)
# rooster.vulRandom()

#randomSteekproef(rooster, 20000)
#
# simulatedAnnealing(rooster, minIteraties, 100, 1, sigmoidalFunctie)
=======
minIteraties = 1000
rooster = Rooster.Rooster(dagen, tijdsloten)
rooster.vulRandom()
# visualiseer(tijdsloten, dagen, rooster)
#randomSteekproef(rooster, 20000)

#simulatedAnnealing(rooster, minIteraties, 100, 1, sigmoidalFunctie)
>>>>>>> cbc0cdb0dd76232192d8c6126590813ff29bf6f5

#
# rooster, scoreLijst = sequential(rooster)
#
# print(scoreLijst)
# scoreLijst = hillClimberSteepestAscent(rooster, 500)
# iteratieVisualisatie(scoreLijst)

<<<<<<< HEAD
rooster = Rooster.Rooster(dagen, tijdsloten)
tweevoudigeMinimalisatie(rooster, 100, 5)

# scoreLijst = []
# iteraties = 20
# for i in range(iteraties):
#     rooster = Rooster.Rooster(dagen, tijdsloten)
#     rooster.vulRandom()
#     nieuwRooster = geneticAlgorithm(rooster, dagen, tijdsloten, 50, 250, 0.25)
#     scoreLijst.append(nieuwRooster[0].score())
#     print("we zijn bij interatie: " + str(i))
#
# frequentieHistogram(scoreLijst)
=======
scoreLijst = []
iteraties = 20
for i in range(iteraties):
    rooster = Rooster.Rooster(dagen, tijdsloten)
    rooster.vulRandom()
    nieuwRooster = sequential(rooster)
    nieuwRooster1 = simulatedAnnealing(nieuwRooster, 200, 100, 1, exponentieelFunctie)
    nieuwRooster2 = hillClimberSteepestAscent(nieuwRooster1, 200)
    scoreLijst.append(nieuwRooster2.score())
    print("we zijn bij iteratie: " + str(i))

frequentieHistogram(scoreLijst)

>>>>>>> cbc0cdb0dd76232192d8c6126590813ff29bf6f5

# #Assuming res is a flat list
# with open("resultaat.csv", "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     for val in nieuwRooster[1]:
#         writer.writerow([val])

# sequential(dagen, tijdsloten)

# groottePopulatie = 10
# aantalGeneraties = 5
# hoi = geneticAlgorithm(rooster, dagen, tijdsloten, groottePopulatie, aantalGeneraties)
#
# hoi.scoreOnderverdeeld()


# rooster = roosterEnScore[0]
# score = roosterEnScore[1]
# visualiseer(tijdsloten, dagen, rooster)

# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, 20000)

<<<<<<< HEAD
# print("WELKOM BIJ HET INPLANNEN VAN DE LESROOSTERS")
# def uitvoer():
#     algoritme = input("Welke algoritme wil je uitproberen? \nJe kunt kiezen uit hillClimber, hillClimber2, simulatedAnnealing, sequential of geneticAlgorithm\n")
#     aantalIteraties = input("Met hoeveel iteraties wil je dit algoritme uitvoeren?\n")
#     print("Cool, laten we " + algoritme + " met " + aantalIteraties +" iteraties uitvoeren!")
#
#     if algoritme == "hillClimber":
#         roosterNieuw, scoreNieuw = hillClimber(rooster, int(aantalIteraties))
#         print(roosterNieuw, scoreNieuw)
#     if algoritme == "hillClimber2":
#         roosterNieuw, scoreNieuw = hillClimber2(rooster, int(aantalIteraties))
#         print(roosterNieuw, scoreNieuw)
#     if algoritme == "simulatedAnnealing":
#         roosterNieuw = (simulatedAnnealing(dagen, tijdsloten))[0]
#         scoreNieuw = (simulatedAnnealing(dagen, tijdsloten))[1]
#
#     nogEenKeer = input("Wil je nog een algoritme op dit rooster uitproberen? (j/n)\n")
#     if nogEenKeer == "j":
#         return uitvoer()
#     else:
#         print("Bedankt! Hopelijk ben je tevreden met je rooster.")
# uitvoer()

# scoreLijst = []
# iteraties = 100
# for i in range(iteraties):
#     rooster = Rooster.Rooster(dagen, tijdsloten)
#     rooster.vulRandom()
#     nieuwRooster = simulatedAnnealing(rooster, 1500)
#     scoreLijst.append(nieuwRooster.score())
#     print(i)
=======
# print("\nWELKOM BIJ HET INPLANNEN VAN DE LESROOSTERS\n")
# def uitvoer(rooster):
#     algoritme = input("Welke algoritme wil je uitproberen? \nJe kunt kiezen uit hillClimberStochastisch, hillClimberSteepestAscent, simulatedAnnealing, sequential of geneticAlgorithm\n")
#
#     if algoritme == "geneticAlgorithm":
#         groottePopulatie = input("Hoe groot moet de populatie zijn?\n")
#         aantalGeneraties = input("Hoeveel generaties moeten er gemaakt worden?\n")
#         mutatieKans = input("Welke mutatiekans moet worden toegepast (getal tussen 0 en 1)?\n")
#
#     if algoritme != "sequential" and algoritme != "geneticAlgorithm":
#         aantalIteraties = input("Met hoeveel iteraties wil je dit algoritme uitvoeren?\n")
#
#     if algoritme == "simulatedAnnealing":
#         beginTemperatuur = input("begin temperatuur: ")
#         eindTemperatuur = input("eind temperatuur: ")
#         temperatuurFunctie = input("Wil je gebruik maken van een lineairFunctie, exponentieelFunctie of sigmoidalFunctie koelschema?\n")
>>>>>>> cbc0cdb0dd76232192d8c6126590813ff29bf6f5
#
#     print("Cool, laten we " + algoritme + " uitvoeren! (Het kan even duren)")
#
#     if algoritme == "hillClimberStochastisch":
#         roosterNieuw, scoreNieuw = hillClimberStochastisch(rooster, int(aantalIteraties))
#     elif algoritme == "hillClimberSteepestAscent":
#         roosterNieuw, scoreNieuw = hillClimberSteepestAscent(rooster, int(aantalIteraties))
#     elif algoritme == "simulatedAnnealing":
#         if temperatuurFunctie == "lineairFunctie":
#             roosterNieuw, scoreNieuw = simulatedAnnealing(rooster, int(aantalIteraties), int(beginTemperatuur), int(eindTemperatuur), lineairFunctie)
#         elif temperatuurFunctie == "exponentieelFunctie":
#             roosterNieuw, scoreNieuw = simulatedAnnealing(rooster, int(aantalIteraties), int(beginTemperatuur), int(eindTemperatuur), exponentieelFunctie)
#         elif temperatuurFunctie == "sigmoidalFunctie":
#             roosterNieuw, scoreNieuw = simulatedAnnealing(rooster, int(aantalIteraties), int(beginTemperatuur), int(eindTemperatuur), sigmoidaFunctie)
#     elif algoritme == "sequential":
#         roosterNieuw, scoreNieuw = sequential(rooster)
#     elif algoritme == "geneticAlgorithm":
#         roosterNieuw, scoreNieuw = geneticAlgorithm(rooster, dagen, tijdsloten, int(groottePopulatie), int(aantalGeneraties), int(float(mutatieKans)))
#
#     print("Rooster: " + str(roosterNieuw) + "\nDit rooster heeft een score van " + str(scoreNieuw[len(scoreNieuw)-1]))
#     nogEenKeer = input("Wil je nog een algoritme op dit rooster uitproberen? (j/n)\n")
#     if nogEenKeer == "j":
#         return uitvoer(roosterNieuw)
#     else:
#         print("Bedankt! Hopelijk ben je tevreden met een rooster van " + str(scoreNieuw[len(scoreNieuw)-1]) + " punten. Het rooster wordt voor je geprint.")
#         visualiseer(tijdsloten, dagen, roosterNieuw)
# uitvoer(rooster)

scoreLijst = []
nieuwRooster = []
iteraties = 50
for i in range(iteraties):
    rooster = Rooster.Rooster(dagen, tijdsloten)
    rooster.vulRandom()
    nieuwRooster = hillClimberStochastisch(rooster, 4000)
    nieuwRooster2 = hillClimberSteepestAscent(rooster, 100)
    scoreLijst.append(nieuwRooster2.score())
    print(i)

frequentieHistogram(scoreLijst)
