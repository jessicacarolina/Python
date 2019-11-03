n = int(input())
fibonacci = 1
cont = 1
vet = [1,1]
vet1 = []
c = 1
while cont <= 1000:
    fibonacci = fibonacci + vet[cont-1]
    vet.append(fibonacci)
    cont = cont + 1
while c <= 1000:
    if c not in vet:
        vet1.append(c)
    c = c + 1

print(vet1[n-1])