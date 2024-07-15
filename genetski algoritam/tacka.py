
""" modul za rad sa tackama """

import random
import math

def generisi_tacke(broj_tacaka):
    """ Funkcija uzima broj tacaka i generise toliko random tacaka """
    tacke = []
    for broj in range(broj_tacaka):
       tacke.append( [random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)] )
    return tacke

def generisi_vrijednosti(tacke):
    """ Funkcija uzima tacke i dodjeljuje im random vrijednosti """
    tacke_vrijednosti = []
    for tacka in tacke:
        tacke_vrijednosti.append( [tacka, random.randint(1, 10)] )
    return tacke_vrijednosti

def regioni_tacaka(tacke, regioni):
    """ Funkcija uzima tacke i regione i rasporedjuje koja tacka pripada kom regionu """
    tacke_regioni=[]
    for k in range( len(tacke) ):
        tacke_regioni.append( [ [tacke[k][0], tacke[k][1]], regioni[k] ] )
    return tacke_regioni

def razdaljina_izmedju_tacaka(tacka1,tacka2):
    """ Funkcija prima dvije tacke i vraca razdaljinu izmedju njih """
    x = tacka1[0] - tacka2[0]
    y = tacka1[1] - tacka2[1]
    return math.sqrt(x**2 + y**2)