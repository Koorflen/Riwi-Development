CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
LF=[]
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
for i in range (len(LN)-1,-1,-1):
    LF.append(LN[i])
print(LN)
print(LF)