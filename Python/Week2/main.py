"""
Hoofdbestand Heuristieken

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import student as studentClass
import zaal as zaalClass
import copy

# initialiseer lijsten met data
studentenLijst = studentClass.studentenLijst
vakkenLijst = studentClass.vakkenLijst

def main():

    # dict om id van tijdsloten om te zetten naar tijd
    idNaarTijdslot = {1 : "9:00-11:00", 2 : "11:00-13:00", 3 : "13:00-15:00", 4 : "15:00-17:00"}

    # dict met alle zalen per dag
    dag = {1 : zaalClass.zaalLijst[:], 2 : zaalClass.zaalLijst[:], 3 : zaalClass.zaalLijst[:], 4 : zaalClass.zaalLijst[:]}

    # weekrooster met tijdslots en zalen
    rooster = {"maandag" : copy.deepcopy(dag), "dinsdag" : copy.deepcopy(dag), "woensdag" : copy.deepcopy(dag), "donderdag" : copy.deepcopy(dag), "vrijdag" : copy.deepcopy(dag)}


if __name__ == "__main__":
    main()
