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
#from hillClimber import hillClimbing
from sequential import sequential
=======
from hillClimber import hillClimbing
from simulatedAnnealing import simulatedAnnealing
# from sequential import sequential, sequentialRandom
>>>>>>> ec28dc3ddd97b3b4ed0a2bc24a3e37999ea30999

#import rooster as Rooster
#from visualiseer import visualiseer

# from randomSteekproef import randomSteekproef
#from geneticAlgorithm import geneticAlgorithm

# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]


# maak een rooster object aan
# rooster = Rooster.Rooster(dagen, tijdsloten)

sequential(dagen, tijdsloten)

<<<<<<< HEAD
=======
# sequential(rooster)

# groottePopulatie = 5
# aantalGeneraties = 3
# geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties)
>>>>>>> ec28dc3ddd97b3b4ed0a2bc24a3e37999ea30999

# vul het rooster met vakken
# rooster.vulRandom()


#rooster.vulRandom()

# rooster.vulRandom()



# hillClimbing(dagen, tijdsloten)
simulatedAnnealing(dagen, tijdsloten)

# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, iteraties)
