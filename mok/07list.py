#Petriuko pazymiai
# Ivedamas pazymiu kiekis ir suvedami pazymiai. rasti vidurki

kiek  = int(input('Kiek Petriukas turi pazymiu? '))
p = []
for i in range(kiek):
    paz = int(input(f'Įveskite {i+1}-ąjį pažymį...'))
    p.append(paz)


print(f'Petriuko pazymiai {p}')

suma = 0
for i in p:
    suma += i
vidurkis = suma / len(p)
print(f'Petriuko vidurkis {vidurkis}')