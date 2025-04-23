N1=str(input("Ingrese su nombre\n"))
Y1=int(input("Ingrese su edad\n"))
N2=str(input("Ingrese su nombre\n"))
Y2=int(input("Ingrese su edad\n"))
if (Y1>=18 and Y2>=18) and (N1!=N2) and ((Y1-Y2)<=10 and (Y2-Y1)<=10):
    print("Felicidades has encontrado a tu alma gemela, casense ya")
elif (Y1>=18 and Y2>=18) and (N1!=N2) and not ((Y1-Y2)<=10 and (Y2-Y1)<=10):
    print("Lo siento no sois almas gemlas, hay mucha diferencia de edad entre vosotros")
elif (Y1>=18 and Y2>=18) and not (N1!=N2) and ((Y1-Y2)<=10 and (Y2-Y1)<=10):
    print("Lo siento no sois almas gemelas, teneis el mismo nombre")
elif not (Y1>=18 and Y2>=18) and (N1!=N2) and ((Y1-Y2)<=10 and (Y2-Y1)<=10):
    print("Lo siento no sois almas gemelas, uno de vosotros es menor de edad o los dos lo sois")