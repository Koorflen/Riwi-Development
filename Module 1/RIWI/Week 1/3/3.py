S=int(input("Ingrese su sueldo bruto\n"))
P=int(input("Ingrese el porcentaje a descontar de su sueldo\n"))
SF=S-(S*P/100)
print(f"Sueldo bruto: {S}\nPorcentaje a descontar: {P}%\nSueldo neto: {SF}")