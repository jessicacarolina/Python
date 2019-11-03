value = float(input("Valor da prestaçao em atraso: "))
acrescimo = value*0.1
total = value + acrescimo
totDesconto = total-(total*0.1)
prejuizo = value - totDesconto
print("Valor a pagar R$%.2f"%(totDesconto))
print("O prejuizo foi de R$%.2f"%(prejuizo))