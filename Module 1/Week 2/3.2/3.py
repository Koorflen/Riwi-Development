CN=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
SC=0
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
print(LN)
for i in LN:
    SC+=i**2
print(SC)