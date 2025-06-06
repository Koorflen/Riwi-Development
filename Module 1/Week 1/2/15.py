X=float(input("Ingresa un numero decimal\n"))
M=["no es negativo o mayor que 100", "es negativo o mayor que 100"]
print(f"{X} {M[X<0 or X>100]}")