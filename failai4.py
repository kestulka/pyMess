def sukurtiBylas(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)

for i in range (1, 11):
    sukurtiBylas(f'{i}byla.txt', f'{i} byloje irasyta informacija \n')

# funkcija skaityti failams

def skaitytiFailus(failu_sarasas):
    for failas in failu_sarasas:
        with open(failas, 'r', encoding='utf-8') as f:
            turinys = f.read()
            print(f'Failas: {failas}\nTurinys:\n{turinys}\n')

# Sukuriamas failų sąrašas
failu_sarasas = [f'{i}byla.txt' for i in range(1, 11)]

# Kviečiama funkcija sukurtais failais
skaitytiFailus(failu_sarasas)


# def kuriam(failas, tekstas):
#     with open(failas,'w',encoding='utf-8') as f:
#         f.write(tekstas)
# def skaitom(failas):
#     with open(failas,'r',encoding='utf-8') as f:
#         txt = f.read()
#     return txt
        
# for i in range(1, 6):
#     kuriam(f'{​​​​​​i}​​​​​​data.txt', f'{​​​​​​i}​​​​​​ byloja irasyta informacija')
#     print(skaitom(f'{​​​​​​i}​​​​​​data.txt'))

