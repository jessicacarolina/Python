nome = input("Digite o nome do aluno: ")
notaA = float(input("Digite a nota A: "))
notaB = float(input("Digite a nota B: "))
media = ((notaA * 2) + notaB)/3
print("A media de {} é %.2f".format(nome)%(media))