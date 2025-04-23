X=float(input("Ingresa un numero\n"))
M=["distinto de 0, y no esta entre 10 y 20", "igual a 0, o es mayor que 10 y menor que 20"]
print(f"Tu numero es {M[X==0 or 10<X<20]}")