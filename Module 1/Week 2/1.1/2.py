X=int(input("Ingresa dos numeros\n"))
Y=int(input())
if X>Y:
    print(f"{X} es mayor que {Y}")
elif Y>X:
    print(f"{Y} es mayor que {X}")
else:
    print(f"{X} y {Y} son iguales")

if X<0:
    print(f"{X} es menor que 0")

if Y<0:
    print(f"{Y} es menor que 0")