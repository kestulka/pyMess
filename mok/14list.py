sar1 = [2, 4, -5, 6, 8, -2, -7, 5]
sar2 = [2, -6, 8, 3, 5, -2, 7]
sarNul = []
for x in sar1:
    for y in sar2:
        sumaNul = x + y
        if sumaNul == 0:
            sarNul.append([x, y])
print(sarNul)

sar0 = [[x, y] for x in sar1 for y in sar2 if x+y == 0]
print(sar0)