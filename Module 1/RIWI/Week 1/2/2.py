X=float(input("Ingresa tres numeros\n"))
Y=float(input())
Z=float(input())
M=["el primero no es menor que el segundo y mayor que el tercero", "el primero es menor que el segundo y mayor que el tercero"]
print(f"De los numeros que ingresaste se concluye que: {M[X<Y and X>Z]}")