X=str(input("Ingresa dos cadenas de texto\n"))
Y=str(input())
M=["Ingresaste cadenas de texto distintas entre si", "Las dos cadenas de texto son exactamente iguales"]
print(f"{M[X==Y]}")