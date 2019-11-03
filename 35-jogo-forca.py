p = input('Palavra: ')
palavra = list(p)
for i in range(0,100):
	print('\n') 
print("A palavra tem ",len(p), 'letras, tente adivinhar!')
acertos = []
erros = 0
digitadas = []
l = input('Digite a primeira letra: ')
exibe = ''
while list(exibe) != palavra:
     if l in digitadas:
         print("Você já tentou esta letra!")
     else:
         digitadas += l
         if l in palavra:
               acertos += l
         else:
               erros += 1
               print("Você errou!")
     exibe = ''
     for letra in palavra:
         exibe += letra if letra in acertos else "."
     print(exibe)
     if list(exibe) != palavra:
             for i in range(0,5):
                print('\n') 
             print('O numero de erros é %d'%(erros))
             l = input('Digite outra letra: ')
     else:
             print("Você ganhou!")
             break
     if erros == 6:
             print("Você perdeu!")
             break
print('Fim de jogo')