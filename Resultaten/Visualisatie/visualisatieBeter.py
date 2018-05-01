"""
Created on Tue May  1 14:22:19 2018

@author: Nadja
"""

import plotly.plotly as py
import plotly.figure_factory as ff
from plotly import tools

maandag = [["<b>Maandag</b>", "A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C0.110"],
           ["09:00-11:00", "bla", "bla", "bla", "bla", "bla", "bla", "bla"]]

dinsdag = [["<b>Dinsdag</b>", "A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C0.110"],
           ["09:00-11:00", "bla", "bla", "bla", "bla", "bla", "bla", "bla"]]

tabel1 = ff.create_table(maandag)
tabel2 = ff.create_table(dinsdag)

figuur = tools.make_subplots(rows = 2, cols = 1, print_grid = True,
                             vertical_spacing = 0.085, subplot_titles("Maandag", "Dinsdag"))

tabel1["data"]
tabel2["data"]

fig.append_trace(table1['data'][0], 1, 1)
fig.append_trace(table2['data'][0], 2, 1)

