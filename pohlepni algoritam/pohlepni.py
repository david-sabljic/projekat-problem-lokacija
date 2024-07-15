
""" modul sa glavnim funkcijama pohlepnog alogritma """

import math

def napravi_krugove(regioni, x, test_point_dist, tacke_regioni):
    """ Funckija koja za odredjeno postrojenje x pravi krugove """
    broj_pomocna = 0
    krugovi = []
    for k in tacke_regioni:
        if k[1] == x:
            krugovi.append( [ [k[0][0], k[0][1]], test_point_dist[broj_pomocna] ] )
        broj_pomocna += 1
    return krugovi

def nadji_presjek_kruznica(x0,y0,r0,x1,y1,r1):
    """ Funkcija prima dva kruga i vraca presijek kruznica tih krugova """
    d = math.sqrt( (x1-x0)**2 + (y1-y0)**2 )
    if d > r0+r1:
        return None
    if d < abs(r0-r1):
        return None
    if d == 0 and r0 == r1:
        return None
    else:
        a = (r0**2-r1**2+d**2)/(2*d)
        h = math.sqrt(r0**2-a**2)
        x2 = x0+a*(x1-x0)/d
        y2 = y0+a*(y1-y0)/d
        x3 = x2+h*(y1-y0)/d
        y3 = y2-h*(x1-x0)/d
        x4 = x2-h*(y1-y0)/d
        y4 = y2+h*(x1-x0)/d
        return [ [x3,y3], [x4,y4] ]
    
def pripada_krugovima(krugovi,x,y):
    """ Funckija za tacku (x,y) vraca listu kojim krguovima pripada """
    rezultat = []
    for krug in krugovi:
        d = math.sqrt( (x-krug[0][0])**2+(y-krug[0][1])**2 )
        if d < krug[1]+0.000000000000000000000001:
            rezultat.append( [ krug[0][0], krug[0][1] ] )
    return rezultat

def pronadji_presjeke(krugovi,postorjenje):
    """ Funkcija koja generise presijeke krugova za sva postrojenja """
    s = []
    if len(krugovi) < 2:
        return [[[ postorjenje[0], postorjenje[1] ]]]
    for k in range( len(krugovi)-1 ):
        for j in range( k+1, len(krugovi) ):
            pomocna = nadji_presjek_kruznica(krugovi[k][0][0], krugovi[k][0][1], krugovi[k][1], krugovi[j][0][0], krugovi[j][0][1], krugovi[j][1])
            if(pomocna != None):
                x = (pomocna[0][0]+pomocna[1][0])/2
                y = (pomocna[0][1]+pomocna[1][1])/2
                s.append( [ [x,y], pripada_krugovima(krugovi, x, y) ] )
    return s

def pomocna_rangiranje(tacke,vrijednosti):
    """ Pomocna funckija koja pronalazi ukupnu vrijednost """
    pomocna = 0
    for k in tacke:
        for j in vrijednosti:
            if( k[0] == j[0][0] and k[1] == j[0][1]):
                pomocna+=j[1]
                break;
    return pomocna

def rangiraj_presjeke(presjeci,vrijednosti):
    """ Funckija koja rangira presjeke u zavisnosti od ukupne vrijednosti dobijene pomocnom funkcijom """
    for k in range( len(presjeci)-1 ):
        for t in range( k+1, len(presjeci) ):
            if( pomocna_rangiranje(presjeci[k][1], vrijednosti) < pomocna_rangiranje(presjeci[t][1], vrijednosti) ):
                pomocna = presjeci[k]
                presjeci[k] = presjeci[t]
                presjeci[t]=pomocna