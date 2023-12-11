# masyve sk tik lyginius
txt = '52, 14, -15, 45, 14, 58, 47, 12, 14, 12, 18, 12, 14, 37, 41, 58, 21, 22'
sk =[int(i) for i in txt.split(', ')  if int(i) % 2 == 0]
# skLyg = [i for i in sk if i % 2 == 0]
# sk = list(set(sk))
print(sk)
# print(skLyg)

