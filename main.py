"""
Hoofd bestand om een rooster object aan te maken en algoritmes te testen.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Resultaten", "Visualisatie"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))


from hillClimber import hillClimber
from hillClimber2 import hillClimber2
from simulatedAnnealing import simulatedAnnealing
from sequential import sequential
from geneticAlgorithm import geneticAlgorithm
import rooster as Rooster
from frequentieHistogram import frequentieHistogram
from iteratieVisualisatie import iteratieVisualisatie
# from visualiseer import visualiseer

# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

# roosterEnScore = hillClimber(dagen, tijdsloten)
# rooster = roosterEnScore[0]
# score = roosterEnScore[1]
# minIteraties = 1000
# rooster = Rooster.Rooster(dagen, tijdsloten)
# rooster.vulRandom()
# # simulatedAnnealing(rooster, minIteraties)
#
# rooster, scoreLijst = hillClimber2(rooster, minIteraties)
# iteratieVisualisatie(scoreLijst)

scoreLijst = []
interaties = 3
for i in range(interaties):
    rooster = Rooster.Rooster(dagen, tijdsloten)
    rooster.vulRandom()
    nieuwRooster = hillClimber(rooster, 1000)
    scoreLijst.append(nieuwRooster[0].score())

frequentieHistogram(scoreLijst)

#sequential(dagen, tijdsloten)

# groottePopulatie = 10
# aantalGeneraties = 5
# hoi = geneticAlgorithm(rooster, dagen, tijdsloten, groottePopulatie, aantalGeneraties)
#
# hoi.scoreOnderverdeeld()

# vul het rooster met vakken
# rooster.vulRandom()
# hillClimbing(dagen, tijdsloten)
# rooster = roosterEnScore[0]
# score = roosterEnScore[1]
# visualiseer(tijdsloten, dagen, rooster, score)


#rooster.vulRandom()

# rooster.vulRandom()

# simulatedAnnealing(dagen, tijdsloten)

# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, iteraties)
# print("WELKOM BIJ HET INPLANNEN VAN DE LESROOSTERS")
# def uitvoer():
#     algoritme = input("Welke algoritme wil je uitproberen? \nJe kunt kiezen uit hillClimber, hillClimber2, simulatedAnnealing, sequential of geneticAlgorithm\n")
#     aantalUivoeren = input("Hoeveel keer wil je dit dit algoritme uitvoeren?\n")
#     print("Cool, laten we " + algoritme + " " + aantalUivoeren +" keer uitvoeren!")
#
#     if algoritme == "hillClimber":
#         rooster = (hillClimbing(dagen, tijdsloten))[0]
#         score = (hillClimbing(dagen, tijdsloten))[1]
#         print(rooster, score)
#     if algoritme == "hillClimber2":
#         rooster = (hillClimbing2(dagen, tijdsloten))[0]
#         score = (hillClimbing2(dagen, tijdsloten))[1]
#     if algoritme == "simulatedAnnealing":
#         rooster = (simulatedAnnealing(dagen, tijdsloten))[0]
#         score = (simulatedAnnealing(dagen, tijdsloten))[1]
#
#     nogEenKeer = input("Wil je nog een algoritme op dit rooster uitproberen? (j/n)\n")
#     if nogEenKeer == "j":
#         return uitvoer()
#     else:
#         print("Bedankt! Hopelijk ben je tevreden met je rooster.")
# uitvoer()
