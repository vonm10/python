rozmery = []
obsah = 500
pocetOperaciA = 0
for a in range(1,501):
    for b in range (1,501):
        if a*b == 500:
            rozmery.append((a,b))
        pocetOperaciA += 1
print(rozmery)
print(pocetOperaciA)
