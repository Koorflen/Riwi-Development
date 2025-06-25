def obtener_condiciones():

    try:
        temperatura = float(input("¿Cual es la temperatura actual (en °C)? "))
    except ValueError:
        print("Por favor, ingresa un numero valido para la temperatura.")
        return None, None

    llueve = input("¿Esta lloviendo? (si/no): ").strip().lower()
    while llueve not in ["sí", "si", "no"]:
        llueve = input("Por favor responde 'si' o 'no': ").strip().lower()

    return temperatura, llueve in ["sí", "si"]


def sugerir_ropa(temperatura, llueve):

    sugerencias = []

    if temperatura <= 10:
        sugerencias.append("abrigo grueso")
        sugerencias.append("ropa de invierno")
    elif 10 < temperatura <= 20:
        sugerencias.append("chaqueta o sueter")
    elif 20 < temperatura <= 28:
        sugerencias.append("ropa ligera")
    else:
        sugerencias.append("ropa muy ligera")
        sugerencias.append("gafas de sol")

    # Lluvia
    if llueve:
        sugerencias.append("lleva paraguas o impermeable")
        sugerencias.append("usa calzado resistente al agua")

    return sugerencias


def mostrar_sugerencias(sugerencias):
    print("\n🔹 Recomendaciones de vestimenta:")
    for item in sugerencias:
        print(f"✔️ {item}")


def asistente_clima():
    print("Bienvenido al Asistente de Clima y Vestimenta")
    temperatura, llueve = obtener_condiciones()

    if temperatura is None:
        print("No se pudo procesar la temperatura.")
        return

    sugerencias = sugerir_ropa(temperatura, llueve)
    mostrar_sugerencias(sugerencias)


asistente_clima()
