def ordenar():
    num1 = int(input("Number: "))
    num2 = int(input("Number: "))
    if num1 > num2:
        return print("In order: %d,%d"%(num1,num2))
    else:
        return print("In order: %d,%d"%(num2,num1))

ordenar()