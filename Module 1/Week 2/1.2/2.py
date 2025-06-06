import datetime
H=datetime.datetime.now().hour
D=datetime.datetime.now().weekday()

if D<5:
        match H:
            case H if 9<=H<12:
                print("¡Es hora de trabajar! Productividad en la mañana.")
            case H if 12<=H<14:
                print("Es hora de descansar un poco, almuerzo.")
            case H if 14<=H<18:
                print("Sigue trabajando, aprovecha la tarde.")
            case _:
                print("Es hora de descansar, ¡es tarde!")
else:
        match H:
            case H if 9<=H<12:
                print("Es un buen momento para hacer ejercicio.")
            case H if 12<=H<14:
                print("Hora de descansar y disfrutar del almuerzo.")
            case H if 14<=H<18:
                print("Disfruta del día, es hora de hacer algo divertido o descansar.")
            case _:
                print("Es hora de relajarte y prepararte para mañana.")