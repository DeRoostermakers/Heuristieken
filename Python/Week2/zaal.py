# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:14:56 2018

@author: Nadja
"""
import copy

class Zaal(object):
    """
    Klasse om een zaal te representeren
    """

    def __init__(self, naam, capaciteit, inGebruik, vak):
        self.naam = naam
        self.capaciteit = capaciteit
        self.inGebruik = inGebruik
        self.vak = vak

    def __str__(self):
        return self.naam

    def __repr__(self):
        return self.naam

# initialiseer alle zalen
zaalLijst = []
zaalLijst.append(Zaal("A1.04", 41, 0, 0))
zaalLijst.append(Zaal("A1.06", 22, 0, 0))
zaalLijst.append(Zaal("A1.08", 20, 0, 0))
zaalLijst.append(Zaal("A1.10", 20, 0, 0))
zaalLijst.append(Zaal("B0.201", 56, 0, 0))
zaalLijst.append(Zaal("C0.110", 117, 0, 0))
zaalLijst.append(Zaal("C1.112", 60, 0, 0))

# dict om id van tijdsloten om te zetten naar tijd
idNaarTijdslot = {1 : "9:00-11:00", 2 : "11:00-13:00", 3 : "15:00-17:00", 4 : "17:00-19:00"}

# dict met alle zalen per dag
dag = {1 : zaalLijst[:], 2 : zaalLijst[:], 3 : zaalLijst[:], 4 : zaalLijst[:]}

# rooster
rooster = {"maandag" : copy.deepcopy(dag), "dinsdag" : copy.deepcopy(dag), "woensdag" : copy.deepcopy(dag), "donderdag" : copy.deepcopy(dag), "vrijdag" : copy.deepcopy(dag)}
