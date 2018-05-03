"""
Functie om de verdeling van scores in te zien middels random sampling.

Linsey Schaap (11036109), Kenneth Goei (11850701), Nadja van 't Hoff (11030720)
"""

def scorefrequentieHistogram(iteraties)

    # simuleer aantal iteraties keer het rooster en onthoud scores
    scores = []
    for simulatie in range(1, iteraties + 1):
        rooster.vulRandom()
        scores.append(rooster.score())
    
    # plot de bargrafiek
    ontwerp = go.Histogram(x=scores, xbins=dict(start=np.min(scores), size=10, end=np.max(scores)),
                       marker=dict(color='rgb(74, 102, 118)'))
    layout = go.Layout(
        title="Histogram met scorefrequentie"
    )
    figuur = go.Figure(data=go.Data([ontwerp]), layout=layout)
    py.plot(figuur, filename='histogram-frequentie')
    
    # 
    mean = np.mean(scores)
    st_dev = np.std(scores)
    median = np.median(scores)
    maximum = np.max(scores)
    minimum = np.min(scores)
    
    print("The mean is " + str(mean))
    print("The standard deviation is " + str(st_dev))
    print("The median is " + str(median))
    print("The maximum is " + str(maximum))
    print("The minimum is " + str(minimum))