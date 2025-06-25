C=int(input("Ingresa tu calificacion\n"))
if C>=60:
    if N>90:
        print("Felicidades aprobaste con la nota mas alta")
    else:
        print("Felicidades aprobaste")
else:
    print(f"Lo lamento, te falto {60-N} para aprobar")