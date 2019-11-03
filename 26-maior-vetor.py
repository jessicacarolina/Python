def maiorVetor(vet):
    maior = vet[0]
    for i in range(0,5):
        if(vet[i] > maior):
            maior = vet[i]
    return maior

vetor = []
for i in range(0,5):
    vetor.append(int(input(("Informe um número: "))))
maior = maiorVetor(vetor)
print("O maior elemento desse vetor é %.2f"%maior)