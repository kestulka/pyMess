import random

# mano sprendimas

# ivestis ir validacija
def lazdu_Zaidimo_Zaideju_Ivestis(kas_Prades, lazdeliu_Kiekis):
    while True:
        try:
            kiek_Paima_Lazdeliu = int(input(f'{kas_Prades}, kiek lazdeliu imate? (nuo 1 iki 3) '))
            if 1 <= kiek_Paima_Lazdeliu <= lazdeliu_Kiekis:
                return kiek_Paima_Lazdeliu
            else:
                print('Liko per mažai lazdelių')
        except ValueError:
            print('Neteisingas įvesties formatas.')

def lazduZaidimas():
    # zaideju vardu ivestis
    zaidejas_1 = input("Įveskite pirmo žaidėjo vardą: ")
    zaidejas_2 = input("Įveskite antro žaidėjo vardą: ")

    # pasirinkti random kuris pradeda
    zaidejai = [zaidejas_1, zaidejas_2]
    lazdeliu_Kiekis = 10
    kas_Prades = random.choice(zaidejai)

    # irasyti pradinius duomenis i txt
    kartu_Suzaista = 0
    while True:
        kartu_Suzaista += 1
        with open("lazdu_zaidimo_eiga.txt", 'a', encoding='utf-8') as f:
            f.write(f'Žaidėjų vardai: {zaidejai[0]} ir {zaidejai[1]}.\n')
            f.write(f'Lazdelių pasirinktas skaičius yra {lazdeliu_Kiekis}.\n')
            f.write(f'Žaidimą pradeda {kas_Prades}\n')
    # zaidimo eiga ir logika
        while lazdeliu_Kiekis > 0:
            print(f'Žaidimą pradeda {kas_Prades}')
            while True:
                try:
                    kiek_Paima_Lazdeliu = lazdu_Zaidimo_Zaideju_Ivestis(kas_Prades, lazdeliu_Kiekis)
                    lazdeliu_Kiekis -= kiek_Paima_Lazdeliu
                    with open("lazdu_zaidimo_eiga.txt", 'a', encoding='utf-8') as f:
                        f.write(f'{kas_Prades} paima {kiek_Paima_Lazdeliu} lazdeles. Liko {lazdeliu_Kiekis}\n')
                    if lazdeliu_Kiekis == 0:
                        laimetojas = zaidejas_1 if kas_Prades == zaidejas_2 else zaidejas_2
                        with open("lazdu_zaidimo_eiga.txt", 'a', encoding='utf-8') as f:
                            f.write(f'Žaidimą laimėjo {laimetojas}.\n')
                        print(f'Žaidimą laimėjo {laimetojas}.\n')
                        break
                    kas_Prades = zaidejas_1 if kas_Prades == zaidejas_2 else zaidejas_2
                    break
                except ValueError: # butina naudojant try:
                    pass 
        # zaidimo kartojimas
        zaidimo_Kartojimas = input("Ar žaisite dar? (taip/ne): ")
        if zaidimo_Kartojimas.lower() == 'ne':
            with open("lazdu_zaidimo_eiga.txt", 'a', encoding='utf-8') as f:
                f.write(f'Į užklausą „Ar žaisite dar“ pasirinko „Ne“\n')
                f.write(f'Žaidimą žaidė {kartu_Suzaista} kartą(us)\n')
            break
        else:
            lazduZaidimas()
 
lazduZaidimas()




# kolegos sprendimas

# def zaidimas(viso_suzaista,ejimai_file):
#     viso_suzaista+=1
#     print("Pradedamas naujas zaidimas. Sekmes!")
#     zaidejas1=input('Pirmo zaidejo vardas: ')
#     zaidejas2=input('Antro zaidejo vardas: ')
#     zaidejai=[zaidejas1, zaidejas2]
#     pradedantis=random.choice(zaidejai)
#     kitas=[p for p in zaidejai if p!=pradedantis][0]
#     visos_lazdeles=int(input('Iveskite su kiek lazdeliu zaisite: '))
#     ejimai_file.write(f'Pradedamas naujas zaidimas.\n')
#     ejimai_file.write(f'Zaideju vardai: {zaidejas1} ir {zaidejas2}.\n')
#     ejimai_file.write(f'Lazdeliu pasirinktas skaicius yra {visos_lazdeles}\n')
#     ejimai_file.write(f'Zaidima pradeda {pradedantis}\n')
#     print(f'Zaideju vardai: {zaidejas1} ir {zaidejas2}.')
#     print(f'Lazdeliu pasirinktas skaicius yra {visos_lazdeles}')
#     print(f'Zaidima pradeda {pradedantis}')
#     while visos_lazdeles>0:
#         paimtos_lazdeles=ejimas(pradedantis,visos_lazdeles,ejimai_file)
#         visos_lazdeles-=paimtos_lazdeles
#         ejimai_file.write(f'{pradedantis} paima {paimtos_lazdeles} lazdeles. Liko {visos_lazdeles}\n')
#         print(f'{pradedantis} paima {paimtos_lazdeles} lazdeles. Liko {visos_lazdeles}')
#         pradedantis,kitas=kitas,pradedantis
#     ejimai_file.write(f'Zaidima laimejo {pradedantis}!\n')
#     print(f'Zaidima laimejo {pradedantis}!')
#     print(f'Nesijaudink {kitas} kita karta labiau pasiseks')
#     return viso_suzaista

# def ejimas(zaidejas,likusios_lazdeles,ejimai_file):
#     galimos_lazdeles=min(3,likusios_lazdeles)
#     paimtos_lazdeles=int(input(f"{zaidejas}, pasirinkite nuo 1 iki {galimos_lazdeles} lazdeliu paimti: "))
#     while paimtos_lazdeles<1 or paimtos_lazdeles>galimos_lazdeles:
#         print(f"Negalimas pasirinkimas. Pasirinkite nuo 1 iki {galimos_lazdeles} lazdeliu.")
#         paimtos_lazdeles=int(input(f"{zaidejas}, pasirinkite nuo 1 iki {galimos_lazdeles} lazdeliu paimti: "))
#     return paimtos_lazdeles

# def kontrolierius():
#     viso_suzaista=0
#     zaisti_dar='Y'
#     with open('reg.txt', 'w') as ejimai_file:
#         while zaisti_dar.upper()=='Y':
#             viso_suzaista=zaidimas(viso_suzaista,ejimai_file)
#             zaisti_dar = input('Ar norite zaisti dar karta? (Y/N): ')
#         ejimai_file.write(f"I uzklausa ,,Ar zaisite dar'' pasirinko ,,Ne''\n")
#         ejimai_file.write(f"Zaidima zaide: {viso_suzaista} karta(us)")
#         print(f'Zaidima zaide: {viso_suzaista} karta(us)')
# kontrolierius()