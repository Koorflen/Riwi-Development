X=int(input("Ingresa tres notas entre 0 y 10\n"))
Y=int(input())
Z=int(input())
if 0<=X<=10 and 0<=Y<=10 and 0<=Z<=10:
    P=(X+Y+Z)/3
    R=["Reprobaste", "Aprobaste"]
    print(R[P>=6])
else:
    print("Notas ingresadas fuera del rango especificado")