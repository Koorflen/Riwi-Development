CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
print(LN)
BN=int(input("Que numero deseas buscar?\n"))
C=0
for i in LN:
    if BN==i:
        C+=1
print(f"El {BN} aparece {C} veces")