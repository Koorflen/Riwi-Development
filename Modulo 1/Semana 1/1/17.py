X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=["Ninguno es mayor a 10", "Almenos uno es mayor que 10"]
print(f"Sobre los numeros que ingresaste concluimos que: {M[X>10 or Y>10]}")