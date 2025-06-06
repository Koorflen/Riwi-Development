X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=["El segundo numero es mayor que el primero", "El primer numero es mayor que el segundo"]
print(f"De los numeros que ingresaste se concluye que: {M[X>Y]}")