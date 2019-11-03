def calc_media(vet):
    m = 0 
    for i in range(0,5):
        m += vet[i]
    m = m/5
    return m

vetor = []
for i in range(0,5):
    vetor.append(int(input("Informe o número: ")))
media = calc_media(vetor)
print("A média é igual a %.2f"%media)