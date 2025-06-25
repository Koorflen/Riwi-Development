O=str(input("ingresa una oracion\n"))
O1=O.replace(",", "")
O2=O.split()
C=0
for i in O2:
    if len(i)>3:
        C+=1
print(f"{C} palabras tienen mas de 3 letras")