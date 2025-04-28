N=int(input("Ingresa un numero\n"))
if N%5==0:
    if N%10==0:
        print("{N} es divisible entre 5 y 10")
    else:
        print("{N} es divisible entre 5")