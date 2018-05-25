"""
Hoofd bestand om een rooster object aan te maken en algoritmes te testen

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))
sys.path.append(os.path.join(directory, "Code", "Visualisatie"))
sys.path.append(os.path.join(directory, "Code", "Functies"))

import rooster as Rooster
from hillClimberStochastisch import hillClimberStochastisch
from hillClimberSteepestAscent import hillClimberSteepestAscent
from simulatedAnnealing import simulatedAnnealing
from simulatedAnnealing import simulatedAnnealing, lineairFunctie, exponentieelFunctie, sigmoidalFunctie
from sequentialEenvoudigeMinimalisatie import sequentialEenvoudigeMinimalisatie
from sequentialTweevoudigeMinimalisatie import sequentialTweevoudigeMinimalisatie
from geneticAlgorithm import geneticAlgorithm
from frequentieHistogram import frequentieHistogram
from iteratieVisualisatie import iteratieVisualisatie
from randomSteekproef import randomSteekproef
from visualiseer import visualiseer

def main():

    # Dagen en tijdsloten welke geldig zijn voor het rooster
    dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
    tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

    rooster = Rooster.Rooster(dagen, tijdsloten)
    rooster.vulRandom()

    print("\nWELKOM BIJ HET INPLANNEN VAN DE LESROOSTERS\n")
    uitvoer(rooster, dagen, tijdsloten)


def uitvoer(rooster, dagen, tijdsloten):

    algoritme = input("Welke algoritme wil je uitproberen?" +
                      "\nJe kunt kiezen uit hillClimberStochastisch, hillClimberSteepestAscent," +
                      "simulatedAnnealing, sequentialEenvoudigeMinimalisatie, " +
                      "sequentialTweevoudigeMinimalisatie of geneticAlgorithm\n")

    if algoritme == "geneticAlgorithm":
        groottePopulatie = input("Hoe groot moet de populatie zijn?\n")
        aantalGeneraties = input("Hoeveel generaties moeten er gemaakt worden?\n")
        mutatieKans = input("Welke mutatiekans moet worden toegepast (getal tussen 0 en 1)?\n")

    if (algoritme != "sequentialEenvoudigeMinimalisatie"
        and algoritme != "geneticAlgorithm"):
        aantalIteraties = input("Met hoeveel iteraties wil je dit algoritme uitvoeren?\n")

    if algoritme == "simulatedAnnealing":
        beginTemperatuur = input("begin temperatuur: ")
        eindTemperatuur = input("eind temperatuur: ")
        temperatuurFunctie = input("Wil je gebruik maken van een lineairFunctie, " +
                                   "exponentieelFunctie of sigmoidalFunctie koelschema?\n")

    if algoritme == "sequentialTweevoudigeMinimalisatie":
        verschilZaal = input("Welk verschil in capaciteit verschil je tussen zalen voor de indeling?\n")

    print("Cool, laten we " + algoritme + " uitvoeren! (Het kan even duren)")

    if algoritme == "hillClimberStochastisch":
        roosterNieuw, scoreNieuw = hillClimberStochastisch(rooster, int(aantalIteraties))
    elif algoritme == "hillClimberSteepestAscent":
        roosterNieuw, scoreNieuw = hillClimberSteepestAscent(rooster, int(aantalIteraties))
    elif algoritme == "simulatedAnnealing":
        if temperatuurFunctie == "lineairFunctie":
            roosterNieuw, scoreNieuw = simulatedAnnealing(rooster, int(aantalIteraties),
                                                          int(beginTemperatuur),
                                                          int(eindTemperatuur),
                                                          lineairFunctie)
        elif temperatuurFunctie == "exponentieelFunctie":
            roosterNieuw, scoreNieuw = simulatedAnnealing(rooster, int(aantalIteraties),
                                                          int(beginTemperatuur),
                                                          int(eindTemperatuur),
                                                          exponentieelFunctie)
        elif temperatuurFunctie == "sigmoidalFunctie":
            roosterNieuw, scoreNieuw = simulatedAnnealing(rooster, int(aantalIteraties),
                                                          int(beginTemperatuur),
                                                          int(eindTemperatuur),
                                                          sigmoidaFunctie)
    elif algoritme == "sequentialEenvoudigeMinimalisatie":
        roosterNieuw, scoreNieuw = sequentialEenvoudigeMinimalisatie(rooster)
    elif algoritme == "sequentialTweevoudigeMinimalisatie":
        roosterNieuw, scoreNieuw = sequentialTweevoudigeMinimalisatie(rooster, int(aantalIteraties), int(verschilZaal))
    elif algoritme == "geneticAlgorithm":
        roosterNieuw, scoreNieuw = geneticAlgorithm(rooster, dagen, tijdsloten,
                                                    int(groottePopulatie),
                                                    int(aantalGeneraties),
                                                    float(mutatieKans))

    print("Rooster: " + str(roosterNieuw) + "\nDit rooster heeft een score van " + str(scoreNieuw[len(scoreNieuw)-1]))
    nogEenKeer = input("Wil je nog een algoritme op dit rooster uitproberen? (j/n)\n")
    if nogEenKeer == "j":
        return uitvoer(roosterNieuw, dagen, tijdsloten)
    else:
        print("Bedankt! Hopelijk ben je tevreden met een rooster van " + str(scoreNieuw[len(scoreNieuw)-1]) + " punten. " +
        "Het rooster wordt voor je geprint.")
        visualiseer(tijdsloten, dagen, roosterNieuw)

if __name__ == "__main__":
    main ()
