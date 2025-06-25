V=float(input("ingrese el monto total de su compra\n"))
Y=int(input("Ingrese su edad\n"))
D=["No obtienes descuento", "Obtienes un descuento en tu compra"]
print(D[V>100 or Y>60])