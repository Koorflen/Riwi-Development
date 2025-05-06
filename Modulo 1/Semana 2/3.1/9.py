N=int(input("Cuantos numeros quieres ingresar?\n"))
LN=[]
M=0
for i in range(N):
    N=int(input(f"ingresa el numero {i+1}: "))
    LN.append(N)
for i in LN:
    for c in LN:
        if i>c:
            M=i
print(f"El numero mas grande es {M}")