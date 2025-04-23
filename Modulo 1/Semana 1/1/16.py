X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=["Ambos no son mayores a 10", "Ambos son mayores que 10"]
print(f"Sobre los numeros que ingresaste decimos que: {M[X>10 and Y>10]}")