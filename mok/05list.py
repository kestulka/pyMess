m = [5, 6, 8, 7, 14, 15, -85, -8, 13, 17]

suma = 0
# for i in m:
#     suma += i
#     i = 10000
# print(suma)
# print(m)
for i in range(len(m)):
    suma += m[i]
    m[i] = 10000

print(suma)
print(m)