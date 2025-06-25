CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
print(LN)
for i in range (CN//2):
    X=LN[i]
    LN[i]=LN[CN-1-i]
    LN[CN-1-i]=X
print(LN)