a = [5, 8, 7, 14, 9]
# reikia masyvo a kvadratu masyvo
b = []
for i in a:
    el = i * i
    b.append(el)
print(b)

c = [i*i*i for i in a]
print(c)

txt = '52, 14, -15, 45, 14, 58, 47, 12'
#listTxt = txt.split(', ')
#print(listTxt)

sk =[int(i) for i in txt.split(', ')]
print(sk)
