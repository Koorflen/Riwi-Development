CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
print(LN)
for i in range (CN):
    for j in range(0,CN-1-i):
        if LN[j]>LN[j+1]:
            X=LN[j]
            LN[j]=LN[j+1]
            LN[j+1]=X
print(LN)