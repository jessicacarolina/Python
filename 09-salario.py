nome = input("Nome do vendedor: ")
numCarros = int(input("Quantidade de carros vendidos: "))
valorTotal = float(input("Valor total das vendas: "))

salario = 500+(50*numCarros)+(valorTotal*(5/100))

print("O salario de {} é %.2f".format(nome)%(salario))