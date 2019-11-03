def op():
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    operacao = input("Digite a operaçao desejada: ")
    if operacao == "+":
        return print("A operaçao escolhida foi soma e o resultado é %.2f"%(num1+num2))
    elif operacao == "-":
        return print("A operaçao escolhida foi subtraçao e o resultado é %.2f"%(num1-num2))
    elif operacao == "/":
        return print("A operaçao escolhida foi divisao e o resultado é %.2f"%(num1/num2))
    elif operacao == "*":
       return print("A operaçao escolhida foi multipicacao e o resultado é %.2f"%(num1*num2)) 
    else:
        
        return print("Operaçao escolhida nao é valida")


op()