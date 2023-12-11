import random

# tautvydo guesseris

# def zaidimas():
#     n = int(input('Iveskite maksimalu skaiciu n:... '))
#     if n <= 0:
#       print('Ivestas netinkamas skaicius, iveskite nauja:...')
#       return
#     sk = random.randint(1, n)
#     spejimai = 0
 
#     while True:
#         spejimas = int(input(f'Atspekite mano skaiciu nuo 1 iki {n}:... '))
#         spejimai += 1
#         if spejimas < 1 or spejimas > n: print(f'Spejimas turi būti nuo 1 iki {n}.')
#         elif spejimas < sk: print(f'mano skaicius didesnis uz {spejimas}.')
#         elif spejimas > sk: print(f'mano skaicius mazesnis uz {spejimas}.')
#         else:
#             print(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
#             break
 
#     kartot = input('Ar norite zaisti dar karta? (t/n): ')
#     if kartot == 't': zaidimas()
#     else: print('Aciu, kad zaidet!')
 
# zaidimas()

def zaidimuxas():
    with open('zaidimo_eiga.txt', 'w') as f:
        zaidimo_Nr = 0
        while True:
            n = int(input('iveskite maksimalu skaiciu: '))
            sk = random.randint(1, n)
            spejimu_Skaicius = 0
            f.write(f'vartotojas ivede skaiciu {n}.\n sugeneruotas atsitiktinis skaicius {sk}.\n')


            while True:
                spejimas = int(input(f'atspeskite mano sugalvota skaiciu nuo 1 iki {n}: '))
                spejimu_Skaicius += 1

                if spejimas < sk:
                    print(f'mano skaicius didesnis uz {spejimas}. \n Jau prasovete {spejimu_Skaicius} spejimus\n')
                    f.write(f'{spejimu_Skaicius} spejimu vartotojas ivede {spejimas}. Atsakymas - sugeneruotas skaicius didesnis\n')
                elif spejimas > sk:
                    print(f'mano skaicius mazesnis uz {spejimas}. \n Jau prasovete {spejimu_Skaicius} spejimus\n')
                    f.write(f'{spejimu_Skaicius} spejimu vartotojas ivede {spejimas}. Atsakymas - sugeneruotas skaicius mazesnis\n')
                else:
                    print(f'sveikinu! atspejote skaiciu {sk} per {spejimu_Skaicius} kartus\n')
                    f.write(f'{spejimu_Skaicius} spejimu vartotojas atspejo skaiciu\n')
                    break
            zaidimo_Nr += 1
            retrig = input('ar zaisite dar karta? (taip/ne)\n').lower()
            f.write(f'i uzklausa "ar zaisite dar" vartotojas pasirinko: "{retrig}" \n')
            if retrig == 'ne':
                break
        f.write(f'vartotojas zaide {zaidimo_Nr} kartus(u)\n')

zaidimuxas()