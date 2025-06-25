X=str(input("Ingresa una palabra\n"))
C=0
for i in X:
    C+=1
M=["mayor a 5 caracteres", "menor o igual a 5 caracteres"]
print(f"{X} tiene una longitug {M[C<=5]}")