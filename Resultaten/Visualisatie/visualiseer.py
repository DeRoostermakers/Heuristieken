"""
Functie om het rooster te visualiseren.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly as py
import plotly.figure_factory as ff
from plotly import tools
py.tools.set_credentials_file(username='DeRoostermakers', api_key='kMZnofKi6pSyYy6Ih1bI')
  
def visualiseer(tijdsloten, weekdagen, rooster):
    
    vanDagNaarID = {"maandag" : 1, "dinsdag" : 2, "woensdag" : 3, "donderdag" : 4, "vrijdag" : 5}
    vanTijdslotNaarID = {"9.00-11.00" : 1, "11.00-13.00" : 2, "13.00-15.00" : 3, "15.00-17.00" : 4, "17.00-19.00" : 5}
    zalen = ["A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C0.112"]
    
    # sorteer activiteiten op dag, tijd en zaal
    gesorteerdeActiviteiten = []
    for dag in weekdagen:
        for tijdslot in tijdsloten:
            for zaalslot in rooster.zaalslotenLijst:
                if vanDagNaarID[dag] == zaalslot.dag:
                    if vanTijdslotNaarID[tijdslot] == zaalslot.tijdslot:
                        if zaalslot.activiteit != None:
                            gesorteerdeActiviteiten.append(zaalslot.activiteit.vakId)
                        else:
                            gesorteerdeActiviteiten.append(None)  

    # zet de data in de juiste weekstructuur
    week = []
    i = 0
    for dag in weekdagen:
        rij = [dag]
        rij.extend(zalen)
        week.append(rij)
        for tijdslot in tijdsloten:
            rij = [tijdslot]
            for zaal in zalen:
                if i < 145:
                    
                    # activiteit niet toevoegen aan niet-toegestane zaalsloten
                    if tijdslot != "17.00-19.00":
                        rij.append(gesorteerdeActiviteiten[i])
                        i += 1
                    elif zaal == "C0.110":
                        rij.append(gesorteerdeActiviteiten[i])
                        i += 1
                    else:
                        rij.append("")
            week.append(rij)

    # maak voor iedere dag een tabel aan
    tabel1 = ff.create_table(week[0:6])
    tabel2 = ff.create_table(week[6:12])
    tabel3 = ff.create_table(week[12:18])
    tabel4 = ff.create_table(week[18:24])
    tabel5 = ff.create_table(week[24:30])
    
    # definieer de vijf subplots
    figuur = tools.make_subplots(rows = 5, cols = 1, print_grid = False,
                                 vertical_spacing = 0.01)
    
    # voeg de tabellen tot de juiste subplot toe
    figuur.append_trace(tabel1["data"][0], 1, 1)
    figuur.append_trace(tabel2["data"][0], 2, 1)
    figuur.append_trace(tabel3["data"][0], 3, 1)
    figuur.append_trace(tabel4["data"][0], 4, 1)
    figuur.append_trace(tabel5["data"][0], 5, 1)
    
    # update de layout van het figuur
    figuur["layout"]["xaxis1"]= dict(figuur["layout"]["xaxis1"], **tabel1["layout"]["xaxis"])
    figuur["layout"]["yaxis1"]= dict(figuur["layout"]["yaxis1"], **tabel1["layout"]["yaxis"])
    figuur["layout"]["xaxis2"]= dict(figuur["layout"]["xaxis2"], **tabel2["layout"]["xaxis"])
    figuur["layout"]["yaxis2"]= dict(figuur["layout"]["yaxis2"], **tabel2["layout"]["yaxis"])
    figuur["layout"]["xaxis3"]= dict(figuur["layout"]["xaxis3"], **tabel3["layout"]["xaxis"])
    figuur["layout"]["yaxis3"]= dict(figuur["layout"]["yaxis3"], **tabel3["layout"]["yaxis"])
    figuur["layout"]["xaxis4"]= dict(figuur["layout"]["xaxis4"], **tabel4["layout"]["xaxis"])
    figuur["layout"]["yaxis4"]= dict(figuur["layout"]["yaxis4"], **tabel4["layout"]["yaxis"])
    figuur["layout"]["xaxis5"]= dict(figuur["layout"]["xaxis5"], **tabel5["layout"]["xaxis"])
    figuur["layout"]["yaxis5"]= dict(figuur["layout"]["yaxis5"], **tabel5["layout"]["yaxis"])
    
    # update de assen wanneer deze niet bij de eerste tabel horen
    for k in range(len(tabel2["layout"]["annotations"])):
            tabel2["layout"]["annotations"][k].update(xref="x2", yref="y2")
    for k in range(len(tabel3["layout"]["annotations"])):
            tabel3["layout"]["annotations"][k].update(xref="x3", yref="y3")
    for k in range(len(tabel4["layout"]["annotations"])):
            tabel4["layout"]["annotations"][k].update(xref="x4", yref="y4")
    for k in range(len(tabel5["layout"]["annotations"])):
            tabel5["layout"]["annotations"][k].update(xref="x5", yref="y5")
          
    figuur["layout"]["annotations"].extend(tabel1["layout"]["annotations"]+tabel2["layout"]["annotations"]
                                            +tabel3["layout"]["annotations"]+tabel4["layout"]["annotations"]
                                            +tabel5["layout"]["annotations"])
    
    # update de layout instellingen van figuur
    figuur["layout"].update(width=800, height=600, margin=dict(t=100, l=50, r=50, b=50), title = "Rooster")
    
    # plot de tabellen
    py.plotly.plot(figuur, filename='Weekrooster')
    
    
