CN=int(input("Cuantos numeros quieres sumar?\n"))
LN=[]
C=0
for i in range(CN):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
for i in LN:
    C+=i
print(f"La suma de todos tus numeros es {C}")
