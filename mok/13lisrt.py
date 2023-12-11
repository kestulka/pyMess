cmAukstis = [186, 185, 168, 147, 205, 158, 198, 174, 158]
colisAukstis = [round(cm/2.45, 2) for cm in cmAukstis]
print(colisAukstis)
# coliai = []
# for i in cmAukstis:
#     el = round(i/2.45, 2)
#     coliai.append(el)
# print(coliai)
# Sukurti eiluciu masyva kur buttu zodelis Aukšt. jei ugis daugiau lygu nei 186 ir vid jei mazesnis zemas kai maziau nei 150
ugisTxt = ['Aukšt.' if i >= 186 else 'Vid.' if i>=150 else 'Žemas'  for i in cmAukstis]
print(ugisTxt)