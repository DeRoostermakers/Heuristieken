"""
Created on Tue May  1 14:22:19 2018

@author: Nadja
"""

import plotly as py
import plotly.figure_factory as ff
from plotly import tools
py.tools.set_credentials_file(username='DeRoostermakers', api_key='kMZnofKi6pSyYy6Ih1bI')


weekdagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag"]
zalen = ["A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C0.110"]

i = 0
for zaalslot in rooster.zaalslotenLijst:
    

# set datastructure
maandag = [["", "A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C0.110"],
           ["09:00-11:00", "1", "2", "3", "bla", "bla", "bla", "bla"],
           ["09:00-11:00", "bla", "bla", "bla", "bla", "bla", "bla", "bla"]]

dinsdag = [["", "A1.04", "A1.06", "A1.08", "A1.10", "B0.201", "C0.110", "C0.110"],
           ["09:00-11:00", "2", "bla", "bla", "bla", "bla", "bla", "bla"],
           ["09:00-11:00", "bla", "bla", "bla", "bla", "bla", "bla", "bla"]]

# define two tables
tabel1 = ff.create_table(maandag)
tabel2 = ff.create_table(dinsdag)

# define the subplots
figuur = tools.make_subplots(rows = 2, cols = 1, print_grid = False,
                             vertical_spacing = 0.085, 
                             subplot_titles = (weekdagen[0], weekdagen[1]))

# add tables to appropriate subplot
figuur.append_trace(tabel1['data'][0], 1, 1)
figuur.append_trace(tabel2['data'][0], 2, 1)

# update layout of figure
figuur['layout']['xaxis1']= dict(figuur['layout']['xaxis1'], **tabel1['layout']['xaxis'])
figuur['layout']['yaxis1']= dict(figuur['layout']['yaxis1'], **tabel1['layout']['yaxis'])
figuur['layout']['xaxis2']= dict(figuur['layout']['xaxis2'], **tabel2['layout']['xaxis'])
figuur['layout']['yaxis2']= dict(figuur['layout']['yaxis2'], **tabel2['layout']['yaxis'])

# update axes of tables other than tabel1
for k in range(len(tabel2['layout']['annotations'])):
        tabel2['layout']['annotations'][k].update(xref='x2', yref='y2')
        
figuur['layout']['annotations'].extend(tabel1['layout']['annotations']+tabel2['layout']['annotations'])

# update layout settings of figuur
figuur['layout'].update(width=800, height=600, margin=dict(t=100, l=50, r=50, b=50), title = "Rooster")

# plot tables
py.plotly.plot(figuur, filename='subplots-table-forum')


