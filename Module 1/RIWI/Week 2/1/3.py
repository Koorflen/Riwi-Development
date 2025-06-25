N=int(input("Ingresa un numero entero\n"))
if N%2==0 and N%3 and N%5==0:
    print(f"{N} es divisible entre 2, 3 y 5")
else:
    print(f"{N} no es divisible entre 2, 3 y 5")