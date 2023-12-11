# def vidurkis_teigiamu_nelyginiu(masyvas):
#     teigiami_nelyginiai = [] 
#     for sk in masyvas:
#         if sk > 0 and sk % 2 != 0:
#             teigiami_nelyginiai.append(sk)

#     if not teigiami_nelyginiai:
#         return "nera teigiamu nelyginiu skaiciu masyve"

#     suma = 0
#     kiekis = 0
#     for sk in teigiami_nelyginiai:
#         suma += sk
#         kiekis += 1

#     vidurkis = suma / kiekis
#     return vidurkis

# ivestis = input("iveskite skaiciu masyva, atskirta tarpais: ")
# ivestos_reiksmes = ivestis.split()

# masyvas = [int(sk) for sk in ivestos_reiksmes]

# rezultatas = vidurkis_teigiamu_nelyginiu(masyvas)
# print("Teigiamu nelyginiu skaiciu vidurkis: ", rezultatas)

def vidurkis_teigiamu_nelyginiu(masyvas):
    teigiami_nelyginiai = []

    for sk in masyvas:
        if sk > 0 and sk % 2 != 0:
            teigiami_nelyginiai.append(sk)

    if not teigiami_nelyginiai:
        return "Nėra teigiamų nelyginių skaičių masyve."

    suma = sum(teigiami_nelyginiai)
    kiekis = len(teigiami_nelyginiai)

    vidurkis = suma / kiekis
    return vidurkis, teigiami_nelyginiai

# Įveskite skaičių masyvą, atskirtą tarpais
ivestis = input("Įveskite skaičių masyvą, atskirtą tarpais: ")
ivestos_reiksmes = ivestis.split()

# Konvertuojame įvestus tekstinius skaičius į sveikuosius skaičius
masyvas = [int(sk) for sk in ivestos_reiksmes]

# Kviečiame funkciją ir išvedame rezultatą
vidurkis, sudedami_skaiciai = vidurkis_teigiamu_nelyginiu(masyvas)
print(f"Teigiamų nelyginių skaičių vidurkis: {vidurkis}")
print(f"Sudedami skaičiai: {sudedami_skaiciai}")



