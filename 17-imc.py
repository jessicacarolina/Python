def imc():
    h= float(input("Digite sua altura: "))
    sexo = input("Sexo (M ou F): ")
    if sexo == "M":
        ideal =  (72.7 * h) - 58
    elif sexo == "F":
        ideal =  (62.1 * h) - 44.7
    else:
        return print("O sexo digitado é invalido, por favor verifique!")
    return print("O ideal seria %.2f"%(ideal))

imc()