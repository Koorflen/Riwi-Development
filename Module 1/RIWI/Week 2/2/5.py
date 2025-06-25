N=str(input("Hello, what's your name?\n"))
D1=int(input(f"\n{N}, what will you do?\n1.Saludar\n2.Despedirse\n3.Salir\n"))
if D1==1:
    print(f"\nHola {N}")
elif D1==2:
    print(f"\nNo te vayas {N} :c")
while D1!=3:

    D1=int(input(f"\n{N}, what will you do?\n1.Saludar\n2.Despedirse\n3.Salir\n"))
    if D1==1:
        print(f"\nHola {N}")
    elif D1==2:
        print(f"\nNo te vayas {N} :c")