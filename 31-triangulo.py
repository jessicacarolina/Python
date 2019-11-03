s1 = float(input('Lado 1: '))
s2 = float(input('Lado 2: '))
s3 = float(input('Lado 3: '))

if s1 > s2 and s1 > s3:
    a = s1
    b= s2
    c = s3
elif s2 > s1 and s2 > s3:
    a = s2
    b = s1
    c = s3
else:
    a = s3
    b = s2
    c = s1
if a >= b+c:
    print('Nenhum triangulo é formado!')
elif a**2 == b**2+c**2:
    print('É um triangulo retangulo!')
elif a**2 > b**2+c**2:
    print('É um triangulo obtusangulo!')
else:
    print('Um triângulo acutângulo é formado!')