"""
Visualisatie rooster als tabel

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly as py
py.tools.set_credentials_file(username='DeRoostermakers', api_key='kMZnofKi6pSyYy6Ih1bI')
import plotly.graph_objs as plot

hoofdregelKleur = "grey"
rijEvenKleur = "lightgrey"
rijOnevenKleur = "white"

ontwerp1 = plot.Table(
        type = "table",
        header = dict(
                values = [["<b>Maandag</b>"],
                          ["A1.04"],
                          ["A1.06"],
                          ["A1.08"],
                          ["A1.10"],
                          ["B0.201"],
                          ["C0.110"],
                          ["C0.110"]],
                line = dict(color = "#506784"),
                            fill = dict(color = hoofdregelKleur),
                            align = ["left", "center"],
                            font = dict(color = "white", size = 12)
                          ),
        cells = dict(
                values = [
                        [["09:00-11:00"], ["11:00-13:00"], ["13:00-15:00"], ["15:00-17:00"], ["17:00-19:00"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]]],
                line = dict(color = "#506784"),
                fill = dict(color = [[rijOnevenKleur, rijEvenKleur, rijOnevenKleur, rijEvenKleur, rijOnevenKleur, rijEvenKleur, rijOnevenKleur]]),
                align = ["left", "center"],
                font = dict(color = "#506784", size = 11)
                        ))
                
ontwerp2 = plot.Table(
        type = "table",
        header = dict(
                values = [["<b>Dinsdag</b>"],
                          ["A1.04"],
                          ["A1.06"],
                          ["A1.08"],
                          ["A1.10"],
                          ["B0.201"],
                          ["C0.110"],
                          ["C0.110"]],
                line = dict(color = "#506784"),
                            fill = dict(color = hoofdregelKleur),
                            align = ["left", "center"],
                            font = dict(color = "white", size = 12)
                          ),
        cells = dict(
                values = [
                        [["09:00-11:00"], ["11:00-13:00"], ["13:00-15:00"], ["15:00-17:00"], ["17:00-19:00"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]],
                        [["bla"], ["bla"], ["bla"], ["bla"], ["bla"]]],
                line = dict(color = "#506784"),
                fill = dict(color = [[rijOnevenKleur, rijEvenKleur, rijOnevenKleur, rijEvenKleur, rijOnevenKleur, rijEvenKleur, rijOnevenKleur]]),
                align = ["left", "center"],
                font = dict(color = "#506784", size = 11)
                        ))



figuur = plot.Figure(data = [ontwerp1, ontwerp2], layout = layout)

py.plotly.plot(figuur, filename = "visualisatieTest")


