CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
LF=[]
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
print(LN)
for i in range (CN):
    if i%2==0:
        LF.append(LN[i])
print(LF)