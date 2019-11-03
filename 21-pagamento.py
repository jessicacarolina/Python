precoEtiqueta = float(input("Preço na etiqueta: "))
print("1 - A vista - 10% ")
print("2 - Cartão - 5%")
print("3 - A prazo 2x - preço normal")
print("4 - A prazo 3x - 10% juros")
forPag = int(input("Digite a forma de pagamento: "))
if forPag == 1:
    total = precoEtiqueta - (precoEtiqueta*0.10)
elif forPag == 2:
    total = precoEtiqueta - (precoEtiqueta*0.05)
elif forPag == 3:
    total = precoEtiqueta
elif forPag == 4:
    total = precoEtiqueta + (precoEtiqueta*0.10)
else:
    print("Forma de pagamento invalida")
print("O total é: %.2f"%(total))