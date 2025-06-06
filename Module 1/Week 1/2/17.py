X=float(input("Ingresa dos edades\n"))
Y=float(input())
M=["Ninguna edad es menor que 18 y la otra mayor que 60", "Alguna edad es menor que 18 y la otra mayor que 60"]
print(f"{M[(X<18 or Y<18) and (X>60 or Y>60)]}")