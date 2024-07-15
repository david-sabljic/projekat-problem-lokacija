
""" Main modul"""

import time
import ispis
import plotovanje
import tacka
import genetski


def dodjeli_klijente_postrojenju(tacke, postrojenja):
    """ Funkcija koja dodjeljuje klijente najblizem postrojenju """
    rezultat = [[] for i in range(len(postrojenja))]
    for i in range(len(tacke)):
         najblize_postrojenje = None
         najmanja_razdaljina = None
         for k in range(len(postrojenja)):
             razdaljina = tacka.razdaljina_izmedju_tacaka(tacke[i],postrojenja[k])
             if najblize_postrojenje == None or najmanja_razdaljina > razdaljina:
                 najblize_postrojenje = k
                 najmanja_razdaljina = razdaljina
         rezultat[najblize_postrojenje].append(tacke[i])
    return rezultat


def alterniraj(postrojenja,klijent_postrojenje):
    """ Funkcija koja ponavlja genetski algoritam sve dok rjesenje nije zadovoljivo """
    uslov=False
    while(uslov==False): 
        nova_postrojenja = genetski.kreiraj_nova_postrojenja(postrojenja, klijent_postrojenje)
        pomocna=1
        for k in range(len(postrojenja)):
            if( abs(postrojenja[k][0]-nova_postrojenja[k][0]) >= 0.001 and abs(postrojenja[k][1]-nova_postrojenja[k][1]) >=0.001 ):
                pomocna = 0
                break
        if pomocna==1:
            uslov=True
        postrojenja=nova_postrojenja.copy()
    return postrojenja


if __name__ == "__main__":
    
    start_time = time.time()
    
    tacke = tacka.generisi_tacke(2000)
    postrojenja = tacka.generisi_tacke(500)
    tacke_vrijednost = tacka.generisi_vrijednosti(tacke)
    klijent_postrojenje = dodjeli_klijente_postrojenju(tacke, postrojenja)
    nova_postrojenja=alterniraj(postrojenja,klijent_postrojenje)
    ispis.ispis(tacke, postrojenja, nova_postrojenja)
    plotovanje.plotuj(tacke, "blue", 5, "o")
    plotovanje.plotuj(postrojenja, "red", 5, "v")
    plotovanje.plotuj(nova_postrojenja, "green", 5, "s")
    
    print("--- %s seconds ---" % (time.time() - start_time))
        


