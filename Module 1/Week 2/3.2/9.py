CN=int(input("Cuantas frases quieres ingresar?\n"))
LN=[]
LF=[]
for i in range(CN):
    N=str(input(f"ingresa la frase {i+1}: "))
    LN.append(N)
print(LN)
for i in range(CN):
    if len(LN[i])>5:
        LF.append(LN[i])
print(LF)