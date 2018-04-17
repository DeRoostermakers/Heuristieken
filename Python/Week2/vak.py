class Vak(object):
    """docstring for [object Object]."""
    def __init__(self, id, naam, hc, wc, maxWc, prac, maxPrac, aantalStudenten):
        self.id = id
        self.naam = naam
        self.hc = hc
        self.wc =  wc
        self.maxWc = maxWc
        self.prac = prac
        self.maxPrac = maxPrac
        self.aantalStudenten = aantalStudenten
        self.studenten = []
