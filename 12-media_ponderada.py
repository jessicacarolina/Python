def media_ponderada():
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    n3 = float(input("Numero 3: "))
    n4 = float(input("Numero 4: "))
    n5 = float(input("Numero 5: "))
    media = n1+(n2*2)+(n3*3)+(n4*4)+(n5*5)/15
    return print("A media ponderada foi de %.2f"%(media))

media_ponderada()