import random
Lis=[1,2,3]
mensage ="N"
while mensage!="Correcto":
    enter=input()
    N1=random.randint(0,2)
    N2=random.randint(0,2)
    N3=random.randint(0,2)
    print(f"{Lis[N1]}|{Lis[N2]}|{Lis[N3]}")
    if N1==N2 and N1==N3:
        mensage="Correcto"
        print(mensage)
    elif N1==N2 and N1!=N3:
        mensage="Casi"
        print(mensage)
    elif N1!=N2 and N1!=N3:
        mensage="Sigue intentando"
        print(mensage)