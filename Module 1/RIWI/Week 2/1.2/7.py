M=str(input("Ingresa un mensaje\n")).lower()

if ("gratis" or "gana dinero" or "descuento exclusivo") in M:
    print("MENSAJE DE SPAM")
else:
    print("Mensaje Seguro")