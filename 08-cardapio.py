print("Cardapio")
print("1 - Hamburguer.....R$3,00")
print("2 - Cheseseburguer.R$2,50")
print("3 - Fritas.........R$2,50")
print("4 - Refrigerante.....R$1,00")
print("5 - Milkshake.....R$3,00")
pedido = int(input("Digite seu pedido: (0 encerra)"))
total = 0
while pedido != 0:
    if pedido == 1:
        qtd = int(input("Quantidade do pedido 1: "))
        total += 3*qtd
    elif pedido == 2:
        qtd = int(input("Quantidade do pedido 2: "))
        total += 2.5*qtd
    elif pedido == 3:
        qtd = int(input("Quantidade do pedido 3: "))
        total += 2.5*qtd
    elif pedido == 4:
        qtd = int(input("Quantidade do pedido 4: "))
        total += 1*qtd
    elif pedido == 5:
        qtd = int(input("Quantidade do pedido 5: "))
        total += 3*qtd
    pedido = int(input("Digite seu pedido: (0 encerra)"))
print("O valor total da conta é R$%.2f"%(total))