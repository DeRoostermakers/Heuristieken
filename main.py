
import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "Classes"))
sys.path.append(os.path.join(directory, "Code", "Algoritmes"))

import rooster as Rooster

dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
tijdsloten = ["9.00-11.00", "11.00-13.00", "13.00-15.00", "15.00-17.00", "17.00-19.00"]

rooster = Rooster.Rooster(dagen, tijdsloten)

print(rooster.vakkenLijst)
print(rooster.studentenLijst)
print(len(rooster.studentenLijst))
print(rooster.idNaarTijdslot)
print(rooster.zaalslotenLijst)
print(len(rooster.zaalslotenLijst))
print(len(rooster.activiteitenLijst))


for vak in rooster.vakkenLijst:
    print(str(vak.id) + "." + str(vak.aantalStudenten))
rooster.vulRandom()

print(rooster.score())
