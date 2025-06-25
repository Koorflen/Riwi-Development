N=int(input("Ingresa un numero\n"))
print("Sus divisores son:")
for i in range (1,N):
    if N%i==0:
        print(i)