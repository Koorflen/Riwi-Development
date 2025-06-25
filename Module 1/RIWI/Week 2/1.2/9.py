N=str(input("Cual es el producto que deeseas compraar?\n"))
V=float(input(f"Cual es el precio de {N}?\n"))
D=int(input("De cuanto es tu descuento?\n"))
P=float(input("Que presupuesto tienes?\n"))

if D!=0:
    VT=V*((100-N)/100)
    if P>VT:
        print("Puedes permitirte comprarlo")
    else:
        print("No puedes permitirte esta compra")
else:
    VT=V
    if P>VT:
        print("Puedes permitirte comprarlo")
    else:
        print("No puedes permitirte esta compra")