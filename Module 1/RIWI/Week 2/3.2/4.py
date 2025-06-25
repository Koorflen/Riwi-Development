CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
LF=[]
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
print(LN)
for i in LN:
    LF.append(i*2)
print(LF)