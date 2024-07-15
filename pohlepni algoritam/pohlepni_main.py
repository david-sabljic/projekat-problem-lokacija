""" Main modul """

from scipy.spatial import Voronoi
from scipy.spatial import cKDTree
import time
import ispis
import tacka
import plotovanje
import pohlepni


def alterniraj(postrojenja, regioni):
    """ Funkcija koja alternira proces pronalazenja novih postrojenja sve dok razlika izmedju postrojenja nije manja od 0.001 """
    uslov = False
    while(uslov == False):
        nova_postrojenja = []
        for k in range( len(postrojenja) ):
            krugovi = pohlepni.napravi_krugove(regioni, k, test_point_dist, tacke_regioni)
            dd = pohlepni.pronadji_presjeke(krugovi, postrojenja[k])
            pohlepni.rangiraj_presjeke(dd, tacke_vrijednost)
            nova_postrojenja.append(dd[0][0])
        pomocna = 1
        for k in range(len(postrojenja)):
            if( abs(postrojenja[k][0]-nova_postrojenja[k][0]) >= 0.001 and abs(postrojenja[k][1]-nova_postrojenja[k][1]) >= 0.001):
                pomocna = 0
                break
        if pomocna == 1:
            uslov = True
        postrojenja=nova_postrojenja.copy()
    return postrojenja


if __name__ == "__main__":
    
    start_time = time.time()
    
    tacke = tacka.generisi_tacke(20)
    postrojenja = tacka.generisi_tacke(5)
    tacke_vrijednost = tacka.generisi_vrijednosti(tacke) 
    vor = Voronoi(postrojenja)
    vor_vertices=vor.vertices
    vor_regioni = vor.regions
    voronoi_kdtree = cKDTree(postrojenja)
    test_point_dist, test_point_regions = voronoi_kdtree.query(tacke)
    tacke_regioni=tacka.regioni_tacaka(tacke, test_point_regions)
    nova_postrojenja=alterniraj(postrojenja, tacke_regioni)
    ispis.ispis(tacke, postrojenja, nova_postrojenja)
    plotovanje.plotuj(tacke, "blue", 5, "o")
    plotovanje.plotuj(postrojenja, "red", 5, "v")
    plotovanje.plotuj(nova_postrojenja, "green", 5, "s")
    
    print("--- %s seconds ---" % (time.time() - start_time))
       




