def abastecer():
    nLitros = float(input("Litros: "))
    combustivel = input("G-gasolina ou A-alcool? ")
    if combustivel == "G":
        p = 3.3
        if nLitros <= 20:
            total = (nLitros * (p-(p*0.04)))
        else:
            total= (nLitros * (p-(p*0.06)))
    elif combustivel == "A":
        p = 2.1
        if nLitros <= 20:
            total= (nLitros * (p-(p*0.03)))
        else:
            total= (nLitros * (p-(p*0.05)))
    else:
        return print("Tipo de combustivel invalido!")
    return print("Total R$%.2f"%(total))
