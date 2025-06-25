X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=["El primer numero es menor que el segundo", "El primer numero es mayor y distinto que el segundo"]
print(f"De los numeros que ingresaste se concluye que: {M[X>Y]}")