CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
C=0
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    if N>0:
        LN.append(N)
for i in LN:
    print(i)