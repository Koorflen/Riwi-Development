N=int(input("Ingresa un numero\n"))
P=True
if N<2:
    P=False
else:
    for i in range(2,N):
        if N%i==0:
            P=False
            break
if P:
    print("Es un numero primo.")
else:
    print("No es primo.")
