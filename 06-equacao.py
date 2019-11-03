a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = (b**2)-(4*a*c)
if delta < 0:
    print("Não existem raizes reais")
elif delta == 0:
    raiz = (-b+(delta**0.5))/(2*a)
    print("Para delta igual a zero, exite uma raiz real igual a %.2f"%(raiz))
else:
    raiz = (-b+(delta**0.5))/(2*a)
    raiz1 = (-b-(delta**0.5))/(2*a)
    print("Para delta igual a %.2f, as raizes são %.2f e %.2f" %(delta,raiz,raiz1))
