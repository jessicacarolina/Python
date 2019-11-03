def tabuada(n):
    tabuada = 'Tabuada\n'
    if n < 10 and n > 0:
        for x in range(1,11):
            y = n * x
            tabuada += str(y)+'\n'
    else:
        tabuada = 'O valor inserido não esta entre 1 e 9!'
    return tabuada
def imc(p,h):
    sPeso = p/(h**2)
    return sPeso
def fatorial(n):
    x = 2
    f = 1
    while x <= n:
        f = f * x
        x = x + 1
    return f

escolha = 0
while escolha != -1:
    print("Escolha")
    print("1 - Tabuada")
    print("2 - IMC")
    print("3 - Fatorial")
    print("-1 - Finaliza")
    escolha = int(input("Opção: "))
    if escolha == 1:
        n = int(input("Número: "))
        print('A tabuada do %d é '%(n)  + '\n'+tabuada(n))
        
    elif escolha == 2:
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        print('O sobrepeso é de %d'%(imc(peso,altura)))
    elif escolha == 3:
        n = int(input("Número: "))
        print('O fatorial de %d é '%(n)+str(fatorial(n)))
    elif escolha == -1:
        print("Programa finalizado!")
    else:
        print("Opção invalida!")