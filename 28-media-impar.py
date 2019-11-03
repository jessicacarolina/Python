def somaImpar(vet):
    soma = 0
    for i in range(0,5):
        if vet[i] % 2 != 0:
            soma += vet[i]
    return soma

vetor = []
for i in range(0,5):
    vetor.append(int(input(("Informe um número: "))))
soma = somaImpar(vetor)
print("O menor elemento desse vetor é %.2f"%soma)
