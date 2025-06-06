P=float(input("Ingresa tu promedio\n"))
I=float(input("Digita tus ingresos,'n"))
M=int(input("ingresa tu cantidad de materias\n"))
B=["Lo lamento, no lograste aplicar a la beca", "Felicidades, has aplicado a la beca"]
print(B[P>=8 and I<=1500 and M<3])