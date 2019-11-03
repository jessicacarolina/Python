print("Escolha a opção abaixo")
print("1 - Calcular o quadrado  de um número")
print("2 - Descobrir se número é par ou impar")
print("3 - Escrever a palavra 'Sonho'")
print("4 - Calcular o salario de um vendedor de carros")
print("5 - Sair do programa")
op = int(input("Opção escolhida: "))
def exe01():
    n = int(input("Digite o número: "))
    return print("O quadrado de %d é %d"%(n,n**2))
def exe02():
    number = int(input("Número: "))
    if number % 2 == 0:
        return print("O numero é par!")
    else:
        return print("O numero é impar!")
def exe03():
    return print("Sonho!")
def exe04():
    nome = input("Nome do vendedor: ")
    numCarros = int(input("Quantidade de carros vendidos: "))
    valorTotal = float(input("Valor total das vendas: "))
    salario = 500+(50*numCarros)+(valorTotal*(5/100))
    return print("O salario de {} é %.2f".format(nome)%(salario))
while op != 5:
    if op == 1:
        exe01()
    elif op == 2:
        exe02()
    elif op == 3:
        exe03()
    elif op == 4:
        exe04()
    op = int(input("Nova opção: "))
print("Programa finalizado")