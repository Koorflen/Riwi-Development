Y=int(input("Ingrese su edad\n"))
N=str(input("ingrese su nacionalidad\n")).lower()
D=int(input("Ingrese su numero de documento\n"))
C=["No cumples los requisitos para participar en el concurso", "Felicidades cumples todos los requisitos para participar del concurso"]
print(C[18<=Y<=30 and N!="antartida" and D!=0])