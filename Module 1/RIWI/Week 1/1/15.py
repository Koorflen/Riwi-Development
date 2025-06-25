X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=["El primer numero es mayor que el segundo", "El primer numero es menor o igual al segundo"]
print(f"De los numeros que ingresaste se puede decir que: {M[X<=Y]}")