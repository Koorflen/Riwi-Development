P=str(input("Ingrese su protocolo (http/https)\n")).lower()
p=int(input("Ingrese su puerto (80/443)\n"))
C=["Su conoexion no es segura", "Su conexion es segura"]
print(C[P=="https" and p==443])