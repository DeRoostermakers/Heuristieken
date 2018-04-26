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
