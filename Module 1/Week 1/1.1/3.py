N=int(input("Ingresa una cantidad de segundos\n"))
H=N//3600
M=(N%100)//60
S=(N-H*3600-M*60)
print(f"{N} Segundos son: {H} horas, {M} minutos, {S} segundos")