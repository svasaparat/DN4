
# TUKAJ UPORABNIK V TERMINAL VNESE ŠTEVILKE, KI SE SHRANIJO V SPREMENLJIVKE
prva_cifra = input("VNESITE 1 ŠTEVILKO \n")
prva_cifra = float(prva_cifra)

druga_cifra = input("VNESITE 2 ŠTEVILKO \n")
druga_cifra = float(druga_cifra)

tretja_cifra = input("VNESITE 3 ŠTEVILKO \n")
tretja_cifra = float(tretja_cifra)

četrta_cifra = input("VNESITE 4 ŠTEVILKO \n")
četrta_cifra = float(četrta_cifra)

peto_cifra = input("VNESITE 5 ŠTEVILKO \n")
peto_cifra = float(peto_cifra)

šesto_cifra = input("VNESITE 6 ŠTEVILKO \n")
šesto_cifra = float(šesto_cifra)

sedmo_cifra = input("VNESITE 7 ŠTEVILKO \n")
sedmo_cifra = float(sedmo_cifra)





# TUKAJ NAŠE SPREMENLJIVKE VNESEMO V LISTO TER IZ NJE IZPIŠEMO MIN, MAX IN ARITMETIČNO SREDINO
def zanimive_vrednosti():
    polje_števil = [prva_cifra, druga_cifra, tretja_cifra, četrta_cifra, peto_cifra, šesto_cifra, sedmo_cifra]

    print("MINIMUM VNESENEGA POLJA ŠTEVIL =", min(polje_števil))

    print("MAKSIMUM VNESENEGA POLJA ŠTEVIL =", max(polje_števil))

    vsota = peto_cifra + druga_cifra + tretja_cifra + četrta_cifra + prva_cifra + šesto_cifra + sedmo_cifra
    dolžina = len(polje_števil)
    aritmetična_sredina = vsota / dolžina
    print("ARITMETIČNA SREDINA POLJA ŠTEVIL =", aritmetična_sredina)






# DA IZPIŠEMO ŠE ZADNJO ZAHTEVO NALOGE; ELEMENT POLJA, KI JE NAJBLIŽJE POVPREČJU; IMAMO NEKAJ VEČ DELA
    # V NOVO LISTO VPIŠEMO ABSOLUTNO RAZLIKO MED SREDINO IN POSAMEZNIMI VNEŠENIMI CIFRAMI
    polje_razlik_med_elemnti_in_aritmetično_sredino = [abs(aritmetična_sredina - prva_cifra), abs(aritmetična_sredina - druga_cifra),
                                                       abs(aritmetična_sredina - tretja_cifra), abs(aritmetična_sredina - četrta_cifra),
                                                       abs(aritmetična_sredina - peto_cifra), abs(aritmetična_sredina -šesto_cifra),

                                                       abs(aritmetična_sredina - sedmo_cifra)]



    # NAJDEMO TISTI ELEMENT, KI IMA NAJMANJŠO RAZLIKO DO POVPREČJA IN GA IZPIŠEMO
    if min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - prva_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", prva_cifra)

    elif min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - druga_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", druga_cifra)

    elif min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - tretja_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", tretja_cifra)

    elif min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - četrta_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", četrta_cifra)

    elif min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - peto_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", peto_cifra)

    elif min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - šesto_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", šesto_cifra)

    elif min(polje_razlik_med_elemnti_in_aritmetično_sredino) == abs(aritmetična_sredina - sedmo_cifra):
        print("NAJBLJIŽJI ELEMENT ARITMETIČNI SREDINI POLJU ŠTEVIL = ", sedmo_cifra)











print(zanimive_vrednosti())

