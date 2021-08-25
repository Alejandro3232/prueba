n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = n2 + 1
if n1 > n2:
    for i in range(n3,n1):
        i = sum(range(n3,n1))
        print("La suma es", end=' ')
        print(i)