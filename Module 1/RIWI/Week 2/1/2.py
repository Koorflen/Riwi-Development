X=float(input("Ingrese tres numeros\n"))
Y=float(input())
Z=float(input())
if X>Y and X>Z:
    print(f"{X} es mayor que {Y} y {Z}")
elif Y>Z and Y>X:
    print(f"{Y} es mayor que {X} y {Z}")
elif X==Y and X==Z and Y==Z:
    print(f"{Z} es mayor que {X} y {Y}")
else:
    print(f"{x}, {Y}, y {Z} son iguales")