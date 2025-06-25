Y=int(input("¿Cuántos años tienes?\n"))
C=str(input("¿Qué tipo de película prefieres? (acción, comedia, terror, otro)\n")).lower()

if Y<13:
        match C:
            case "acción":
                print("Recomendación: 'Las aventuras de Tintín' (película de acción apta para niños)")
            case "comedia":
                print("Recomendación: 'Mi villano favorito' (comedia apta para niños)")
            case "terror":
                print("Recomendación: 'Monster Inc.' (comedia de terror amigable para niños)")
            case _:
                print("Recomendación: 'Toy Story' (película familiar)")
else:
        match C:
            case "acción":
                print("Recomendación: 'Avengers: Endgame' (película de acción)")
            case "comedia":
                print("Recomendación: 'La boda de mi mejor amigo' (comedia)")
            case "terror":
                print("Recomendación: 'El conjuro' (terror)")
            case _:
                print("Recomendación: 'Inception' (película de ciencia ficción)")
