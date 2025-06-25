N=float(input("Ingresa un numero\n"))
if N>0:
    if N>100:
        print(f"{N} es mayor a 100")
elif N<0:
    if N<-50:
        print(f"{N} es menor que -50")
else:
    print("Tu numero es 0")