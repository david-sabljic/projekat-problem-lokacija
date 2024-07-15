""" Modul za genetski algoritam """
import random
import tacka

def kreiraj_nova_postrojenja(postrojenja,klijent_postrojenje):
    """ Funkcija koja pokrece genetski algoritam za kreiranje novih postrojenja """
    nova_postrojenja=[ [] for k in range(len(postrojenja)) ]
    for k in range(len(postrojenja)):
        nova_postrojenja[k] = genetski_algoritam(postrojenja[k], klijent_postrojenje[k], 10, 20)
    return nova_postrojenja

def genetski_algoritam(postrojenje,tacke,velicina_populacije,broj_ponavljanja):
    """ Funkcija koja koristeeci pomocne funkcije vraca novo postrojenje """
    if len(tacke)==0:
        return postrojenje
    populacija = kreiraj_populaciju(postrojenje, velicina_populacije)
    populacija = rankiranje_populacije(populacija, tacke);
    postrojenje1 = populacija[0]
    postrojenje2 = populacija[1]
    for i in range(broj_ponavljanja-1):
        populacija = mutiraj_populaciju(postrojenje1,postrojenje2, velicina_populacije)
        populacija = rankiranje_populacije(populacija, tacke);
        postrojenje1 = populacija[0]
        postrojenje2 = populacija[1]
    return postrojenje1

def kreiraj_populaciju(postrojenje,velicina_populacije):
    """ Funkcija koja kreira populaciju """
    populacija = []
    for k in range(velicina_populacije):
        pomocna1 = random.uniform(-1.0,1.0)/(10**random.randint(0, 9))
        pomocna2 = random.uniform(-1.0,1.0)/(10**random.randint(0, 9))
        populacija.append([postrojenje[0]+pomocna1,postrojenje[1]+pomocna2])
    return populacija

def rankiranje_populacije(populacija, tacke):
    """ Funkcija koja rankira populaciju po razdaljini"""
    populacija_sa_razdaljinom = razdaljina_populacije(populacija,tacke)
    for i in range(len(populacija)-1):
        for k in range(i,len(populacija)):
            if populacija_sa_razdaljinom[i][1]>populacija_sa_razdaljinom[k][1]:
                pomocna=populacija[k]
                populacija[k]=populacija[i]
                populacija[i]=pomocna
                pomocna=populacija_sa_razdaljinom[k]
                populacija_sa_razdaljinom[k]=populacija_sa_razdaljinom[i]
                populacija_sa_razdaljinom[i]=pomocna
    return populacija

def razdaljina_populacije(populacija,tacke):
    """ Funkcija koja vraca razdaljinu populacije od tacaka """
    rezultat = [[] for i in populacija]
    for k in range(len(populacija)):
        pomocna=0
        for i in range(len(tacke)):
            pomocna+=tacka.razdaljina_izmedju_tacaka(tacke[i], populacija[k])
        rezultat[k].append(populacija[k])
        rezultat[k].append(pomocna)
    return rezultat

def mutiraj_populaciju(postrojenje1,postrojenje2,velicina_populacije):
    """ Funkcija za mutiranje populacije """
    populacija = []
    populacija.append(postrojenje1)
    populacija.append(postrojenje2)
    for k in range(2,velicina_populacije):
        pomocna1 = random.uniform(-1.0,1.0)/(10**random.randint(0, 9))
        pomocna2 = random.uniform(-1.0,1.0)/(10**random.randint(0, 9))
        populacija.append([(postrojenje1[0]/postrojenje2[0])+pomocna1,(postrojenje1[1]/postrojenje2[1])+pomocna2])
    return populacija
