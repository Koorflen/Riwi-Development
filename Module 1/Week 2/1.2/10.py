P=input("Ingresa tu contraseña: ")
M=[]

if len(P)<8:
    M.append("❌ Al menos 8 caracteres")
if not any(c.isalpha() for c in P):
    M.append("❌ Debe tener letras")
if not any(c.isdigit() for c in P):
    M.append("❌ Debe tener números")
if " " in P:
    M.append("❌ No debe tener espacios")

if M:
    print("🔐 Contraseña insegura:")
    for i in M:
        print(i)
else:
    print("✅ ¡Contraseña segura!")
