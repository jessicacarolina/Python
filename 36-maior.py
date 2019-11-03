n, n1 ,n2 = input().split()
a = int(n)
b = int(n1)
c = int(n2)
if a > b and a > c:
    print('%d eh o maior'%(a))
elif b > a and b > c:
    print('%d eh o maior'%(b))
else:
    print('%d eh o maior'%(c))