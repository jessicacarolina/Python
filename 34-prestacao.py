def valorPagamento(prestacao,dias):
    if dias != 0:
        total = prestacao+(prestacao*0.03)+(0.1*dias)
    else:
        total = prestacao
    return total

t = 0
qtd = 0
v = float(input("Valor da prestação:"))
d = int(input("Dias em atraso: "))
while v != 0:
    valor = valorPagamento(v,d)
    v = float(input("Valor da prestação - 0 encerra: "))
    d = int(input("Dias em atraso: "))
    t  = t + valor
    qtd = qtd + 1
print("O quantidade foi %d e o total das prestações foi R$%.2f."%(qtd,t))