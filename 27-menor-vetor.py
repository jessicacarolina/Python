def menorVetor(vet):
    menor = vet[0]
    for i in range(0,5):
        if(vet[i] < menor):
            menor = vet[i]
    return menor

vetor = []
for i in range(0,5):
    vetor.append(int(input(("Informe um número: "))))
menor = menorVetor(vetor)
print("O menor elemento desse vetor é %.2f"%menor)