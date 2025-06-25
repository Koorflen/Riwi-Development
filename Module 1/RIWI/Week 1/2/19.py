X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=["No son multiplos", "Son multiplos"]
print(f"De los numeros que ingresaste se concluye que: {M[(X%Y)==0 or (Y%X)==0]}")