T=int(input("Ingrese una cantidad de minutos\n"))
D=T//1440
H=(T-(D*1440))//60
M=(T-H*60-D*1440)
print(f"{T} minutos son: {D} dias, {H} horas y {M} minutos")