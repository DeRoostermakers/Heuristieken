"""
Visualisatie rooster als tabel

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

import plotly as py
py.tools.set_credentials_file(username='DeRoostermakers', api_key='kMZnofKi6pSyYy6Ih1bI')
import plotly.graph_objs as go

headerColor = "grey"
rowEvenColor = "lightgrey"
rowOddColor = "white"

trace0 = go.Table(
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
                            fill = dict(color = headerColor),
                            align = ["left", "center"],
                            font = dict(color = "white", size = 12)
                          ),
        cells = dict(
                values = [
                        [["09:00-11:00"], ["11:00-13:00"]],
                        [["bla"], ["bla"]],
                        [["bla"], ["bla"]],
                        [["bla"], ["bla"]],
                        [["bla"], ["bla"]],
                        [["bla"], ["bla"]],
                        [["bla"], ["bla"]],
                        [["bla"], ["bla"]]],
                line = dict(color = "#506784"),
                fill = dict(color = [[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]]),
                align = ["left", "center"],
                font = dict(color = "#506784", size = 11)
                        ))

data = [trace0]

py.plotly.plot(data, filename = "visualisatieTest")


