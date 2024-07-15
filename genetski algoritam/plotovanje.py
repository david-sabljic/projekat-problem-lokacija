
""" modul za plotovanje rezultata """

import matplotlib.pyplot as plt

def plotuj(tacke, boja, velicina, oblik):
    """ Funkcija uzima tacke, boju, velicinu i oblik i plotuje sa tim parametrima """
    x_kord=[]
    y_kord=[]
    for k in tacke:
        x_kord.append(k[0])
        y_kord.append(k[1])
    plt.plot( x_kord, y_kord, color = "none", markersize = velicina, marker = oblik, markerfacecolor = boja )
