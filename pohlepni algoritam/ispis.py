
""" modul za ispis rezultata """

import sys

def ispis(klijenti, postrojenja, nova_postrojenja):
    """ Funkcija koja ispisuje rezultat """
    print("* Klijenti:")
    for klijent in klijenti:
        print( "(" + str(klijent[0]) + ", " + str(klijent[1]) + ")" )     
    print("* Pocetna postrojenja:")
    for postrojenje in postrojenja:
        print( "(" + str(postrojenje[0]) + ", " + str(postrojenje[1]) + ")" )  
    print("* Nova postrojenja:")
    for postrojenje in nova_postrojenja:
        print( "(" + str(postrojenje[0]) + ", " + str(postrojenje[1]) + ")" )

def ispis_u_fajl(klijenti, postrojenja, nova_postrojenja,fajl,vreme):
    """ Funkcija koja ispisuje rezultat u fajl """
    with open(fajl, 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        print("* Klijenti:")
        for klijent in klijenti:
            print( "(" + str(klijent[0]) + ", " + str(klijent[1]) + ")" )     
        print("* Pocetna postrojenja:")
        for postrojenje in postrojenja:
            print( "(" + str(postrojenje[0]) + ", " + str(postrojenje[1]) + ")" )  
        print("* Nova postrojenja:")
        for postrojenje in nova_postrojenja:
            print( "(" + str(postrojenje[0]) + ", " + str(postrojenje[1]) + ")" )
        print("--- %s seconds ---" % vreme)
        sys.stdout = original_stdout