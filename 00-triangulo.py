l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3= float(input("Terceiro lado: "))
if l1+l2 > l3 and l1+l3 > l2 and l3+11 > l2:
    if l1 == l2 and l1 == l3:
        tipo = "equilatero"
    elif l1 != l2 and l1 != l3 and l3 != l1:
        tipo = "escaleno"
    else:
        tipo = "isosceles"
    print("O triangulo é: %s"%(tipo))
else:
    print("Não forma um triangulo!")