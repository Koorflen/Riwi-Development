X=float(input("Ingresa tres numeros\n"))
Y=float(input())
Z=float(input())
M=["Tus numeros son distintos a 0", "Almenos uno de tus numeros es igual 0"]
print(f"{M[X==0 or Y==0 or Z==0]}")