N=int(input("Ingresa un numero de tres cifras\n"))
print(f"Tu numero es {N}")
C=N//100
D=(N%100)//10
U=N-(C*100+D*10)
print(f"Tu numero invertido es {U}{D}{C}")