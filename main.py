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
=======
# from hillClimber import hillClimbing
# from simulatedAnnealing import simulatedAnnealing
# from sequential import sequential, sequentialRandom
>>>>>>> 594afd79fe94b55c70c95ad5cb4fc59c257867f3

#import rooster as Rooster
#from visualiseer import visualiseer

# from randomSteekproef import randomSteekproef
from geneticAlgorithm import geneticAlgorithm

# Dagen en tijdsloten welke geldig zijn voor het rooster
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]


# maak een rooster object aan
# rooster = Rooster.Rooster(dagen, tijdsloten)

<<<<<<< HEAD
sequentialTres(dagen, tijdsloten)

# sequential(rooster)

# groottePopulatie = 5
# aantalGeneraties = 3
# geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties)
=======
# sequential(dagen, tijdsloten)

# sequential(rooster)

groottePopulatie = 5
aantalGeneraties = 3
geneticAlgorithm(dagen, tijdsloten, groottePopulatie, aantalGeneraties)
>>>>>>> 594afd79fe94b55c70c95ad5cb4fc59c257867f3

# vul het rooster met vakken
# rooster.vulRandom()


#rooster.vulRandom()

# rooster.vulRandom()



# hillClimbing(dagen, tijdsloten)
<<<<<<< HEAD
#simulatedAnnealing(dagen, tijdsloten)
=======
# simulatedAnnealing(dagen, tijdsloten)
>>>>>>> 594afd79fe94b55c70c95ad5cb4fc59c257867f3

# maak een random steekproef aan van x iteraties
# iteraties = 51
# randomSteekproef(rooster, iteraties)
