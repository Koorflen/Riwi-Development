X=int(input("Ingresa un numero entero\n"))
M=["no es divisible entre 5", "es divisible entre 5"]
print(f"Tu numero {M[X%5==0]}")