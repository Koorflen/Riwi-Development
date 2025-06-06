X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=[f"No complen alguna de estas condiciones\nSer distintos entre si\n{X} debe ser mayor que 5", f"Los numeros son distintos entre si y {X} es mayor que 5"]
print(f"De los numeros que ingresaste se concluye que: {M[X!=Y and X>5]}")