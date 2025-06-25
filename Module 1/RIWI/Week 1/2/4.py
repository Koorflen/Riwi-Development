X=float(input("Ingresa un numero\n"))
M=["Es igual a 0 o a 1", "No es igual ni a 0 ni a 1"]
print(f"Del numero que ingresaste se concluye que: {M[not(X==0 or X==1)]}")