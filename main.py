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



from hillClimber import hillClimbing
from simulatedAnnealing import simulatedAnnealing
from sequential import sequential, sequentialDos, sequentialTres
# from geneticAlgorithm import geneticAlgorithm
#import rooster as Rooster
#from visualiseer import visualiseer


from hillClimber2 import hillClimbing2


# from sequential import sequential, sequentialRandom

# import rooster as Rooster
#from visualiseer import visualiseer



# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

# rooster = hillClimbing(dagen, tijdsloten)

# print("HOOOOOI")
# print(rooster.zaalslotenLijst)

# sequential(dagen, tijdsloten)

# sequential(rooster)

#
# groottePopulatie = 5
# aantalGeneraties = 3
# geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties)



# vul het rooster met vakken
# rooster = Rooster.Rooster(dagen, tijdsloten)
# rooster.vulRandom()
# visualiseer(tijdsloten, dagen, rooster)


# hillClimbing(dagen, tijdsloten)
# hillClimbing2(dagen, tijdsloten)
# simulatedAnnealing(dagen, tijdsloten)


# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, iteraties)
print("WELKOM BIJ HET INPLANNEN VAN DE LESROOSTERS")
algoritme = input("Welke algoritme wil je uitproberen? \nJe kunt kiezen uit hillClimber, hillClimber2, simulatedAnnealing, sequential of geneticAlgorithm\n")
aantalUivoeren = input("Hoeveel keer wil je dit dit algoritme uitvoeren?\n")
print("Cool, laten we " + algoritme + " " + aantalUivoeren +" keer uitvoeren!")
if algoritme == "hillClimber":
    rooster = (hillClimbing(dagen, tijdsloten))[0]
    score = (hillClimbing(dagen, tijdsloten))[1]
    print(rooster, score)
if algoritme == "hillClimber2":
    rooster = (hillClimbing2(dagen, tijdsloten))[0]
    score = (hillClimbing2(dagen, tijdsloten))[1]
if algoritme == "simulatedAnnealing":
    rooster = (simulatedAnnealing(dagen, tijdsloten))[0]
    score = (simulatedAnnealing(dagen, tijdsloten))[1]
print("Wil je nog een algoritme op dit rooster uitproberen?")
