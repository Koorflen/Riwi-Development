import random
N=random.randint(1, 100)
I=int(input("Adivina el numero secreto\n"))
while I!=N:
    if I<N:
        print("Un poco mas arriba")
    elif I>N:
        print("Un poco mas abajo")
    I=int(input("Adivina el numero secreto\n"))
print("FELICIDADES")