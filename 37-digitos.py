'''
Dados dois números inteiros, n e m, quantos dígitos tem nm ?
Exemplos:
2 e 10 - 210 = 1024 - 4 dígitos
3 e 9 - 39 = 19683 - 5 dígitos
Entrada
A entrada é composta por vários casos de teste. A primeira linha tem um número inteiro C, representando a quantidade de casos de teste. As C linhas seguintes contém dois números inteiros N e M (1 <= N, M <= 100).
Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número inteiro contendo a quantidade de dígitos do resultado da potência calculada no respectivo caso de teste.
'''
c = int(input())
cont = 1
me = ''
while c >= cont:
    n,m = input().split()
    t = int(n)**int(m)
    if(c == cont):
        me = me + str((len(str(t))))
    else:
        me = me + str((len(str(t))))+'\n' 
    cont = cont + 1 
print(me)