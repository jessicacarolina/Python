def maior(x):
    maior = x[0]
    for i in range(0,30):
        if maior < x[i]:
            maior = x[i]
    return maior
def segundoMaior(y, m):
    sMaior = y[0]
    index = y.index(m)
    for i in range(0,30):
        if i != index and sMaior < y[i]:
            sMaior = y[i]
    return sMaior


import random
vet = []
for i in range(0,30):
    vet.append(random.randint(1,100))
m1 = maior(vet)
sM = segundoMaior(vet,m1)
print(vet)
print("Maior: %d , Segundo maior %d"%(m1,sM))