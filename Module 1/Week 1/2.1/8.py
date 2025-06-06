P=str(input("Cree una contraseña\n"))
V=["Su cotraseña es poco segura", "Su contraseña es segura"]
print(V[len(P)>=8 and "123" not in P])