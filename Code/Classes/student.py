"""
Student klasse

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

class Student(object):

    def __init__(self, achternaam, voornaam, studentnummer, vakken):
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.studentnummer = studentnummer
        self.vakken = vakken

    def __str__(self):
        return self.studentnummer

    def __repr__(self):
        return self.studentnummer
