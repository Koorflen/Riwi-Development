X=float(input("Ingresa tres numeros\n"))
Y=float(input())
Z=float(input())
M=["Algun numero es igual a otro", "Todos son distintos entre si"]
print(f"De los numeros que ingresaste se concluye que: {M[X!=Y and X!=Z and Y!=Z]}")