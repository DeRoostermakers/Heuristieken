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

<<<<<<< HEAD

from hillClimber import hillClimbing
from simulatedAnnealing import simulatedAnnealing
from sequential import sequential, sequentialDos, sequentialTres
from geneticAlgorithm import geneticAlgorithm
#import rooster as Rooster
#from visualiseer import visualiseer
=======
from hillClimber import hillClimbing
<<<<<<< HEAD
from hillClimber2 import hillClimbing2
from simulatedAnnealing import simulatedAnnealing
=======
# from hillClimber2 import hillClimbing2
# from simulatedAnnealing import simulatedAnnealing
>>>>>>> 10692ec1a02dc52e3d4181d04bed62fbdb3f5385
# from sequential import sequential, sequentialRandom

import rooster as Rooster
from visualiseer import visualiseer
>>>>>>> 924a87290306d2bac03670ff016e149efceabf4e



# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

rooster = hillClimbing(dagen, tijdsloten)

print("HOOOOOI")
print(rooster.zaalslotenLijst)

# sequential(dagen, tijdsloten)

# sequential(rooster)
<<<<<<< HEAD

groottePopulatie = 2
aantalGeneraties = 1
geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties)
=======
#
# groottePopulatie = 5
# aantalGeneraties = 3
# geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties)
>>>>>>> 924a87290306d2bac03670ff016e149efceabf4e


# vul het rooster met vakken
# rooster = Rooster.Rooster(dagen, tijdsloten)
# rooster.vulRandom()
visualiseer(tijdsloten, dagen, rooster)

<<<<<<< HEAD
#hillClimbing(dagen, tijdsloten)
=======
# hillClimbing(dagen, tijdsloten)
<<<<<<< HEAD
# hillClimbing2(dagen, tijdsloten)
simulatedAnnealing(dagen, tijdsloten)
=======
>>>>>>> 924a87290306d2bac03670ff016e149efceabf4e
# simulatedAnnealing(dagen, tijdsloten)
>>>>>>> 10692ec1a02dc52e3d4181d04bed62fbdb3f5385

# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, iteraties)
