n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("Em ordem decrecente: %d,%d,%d"%(n1,n2,n3))
    else:
        print("Em ordem decrecente: %d,%d,%d"%(n1,n3,n2))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print("Em ordem decrecente: %d,%d,%d"%(n2,n1,n3))
    else:
        print("Em ordem decrecente: %d,%d,%d"%(n2,n3,n1))
else:
    if n2 > n1:
        print("Em ordem decrecente: %d,%d,%d"%(n3,n2,n1))
    else:
        print("Em ordem decrecente: %d,%d,%d"%(n3,n1,n2))