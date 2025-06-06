GF={}

while True:
    try:
        IM=float(input("Digita tus ingresos mensuales\n"))
        if IM<0:
            print("Por favor, ingresa un valor positivo")
        else:
            break
    except ValueError:
        print("Entrada invalida, ingresa un numero valido")

while True:
    try:
        CGF=int(input("Cuantos gastos fijos tienes?\n"))
        if CGF<=0:
            print("Por favor, ingresa un valor positivo")
        else:
            break
    except ValueError:
        print("Entrada invalida, ingresa un numero valido")

for i in range (CGF):
    while True:
        try:
            K=str(input(f"Cual es su gasto fijo numero {i+1}?\n"))
            V=float(input(f"Ingrese el valor del gasto fijo {K}\n"))
            if V<0:
                print("El valor del gasto no puede ser negativo")
            else:
                GF[K]=V
                break
        except ValueError:
            print("Entrada invalida, ingresa un numero valido")
            
TG=sum(GF.values())
AH=IM-TG

print("\n----Resumen del presupuesto----")
print(f"Ingresos mensuales: ${IM:.2f}")
print("Gastos fijos:")
for gasto, valor in GF.items():
    print(f"- {gasto}: ${valor:.2f}")

print(f"Total de gastos fijos: ${TG:.2f}")

if AH>0:
    print(f"¡Puedes ahorrar ${AH:.2f} este mes!")
elif AH==0:
    print("No tienes dinero extra este mes para ahorrar")
else:
    print(f"Te falta ${abs(AH):.2f} para cubrir todos tus gastos fijos. Necesitas reducir tus gastos")
    