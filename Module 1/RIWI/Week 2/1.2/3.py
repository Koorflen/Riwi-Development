import random

users={"Koorflen": "DIEGOOMG:", "1110483065": "Alejandro1110*"}

user=input("Ingresa tu nombre de usuario\n")


if user in users:

    pasword=input("Ingresa tu contraseña\n")

    if pasword==users[user]:
        print("Contraseña correcta. Generando código de verificación...")

        CV=random.randint(000, 999)
        print(f"Código de verificación generado: {CV}")
        CI=int(input("Ingresa el código de verificación\n"))

        if CI==CV:
            print("Acceso concedido. Bienvenido!")
        else:
            print("Código incorrecto. Acceso denegado")
    else:
        print("Contraseña incorrecta. Acceso denegado")
else:
    print("Usuario no encontrado. Acceso denegado")