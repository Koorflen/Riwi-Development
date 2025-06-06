puntaje=0
P1=str(input("Eres mujer?(si/no)\n")).lower()
if P1=="si":
    P2=int(input("Cuantos años tienes?\n"))
    if 16<=P2<=25:
        puntaje+=10
    elif 35>P1>25:
        puntaje-=80
    else:
        puntaje-=1000
    P3=str(input("La longitud de tu cabello es larga, media o corta?\n")).lower()
    if P3=="larga":
        puntaje+=30
    elif P3=="media":
        puntaje+=20
    elif P3=="corta":
        puntaje+=10
    P4=int(input("Cuanto mides en centimetros?\n"))
    if 165<=P4<=174:
        puntaje+=20
    elif 158<=P4<165 or 175<=P4<=185:
        puntaje+=10
    else:
        puntaje-=10
    P5=str(input("Eres aseada?(si/no)\n")).lower()
    if P5=="si":
        puntaje+=20
    else:
        puntaje-=10
        P6=str(input("Almenos te bañas?(si/no)\n")).lower()
        if P6=="si":
            puntaje+=5
        P7=str(input("Te cepillas minimo 3 veces al dia?(si/no)\n")).lower()
        if P7=="si":
            puntaje+=3
        P8=str(input("Te lavas el cabello cada 2 dias o menos?(si/no)")).lower()
        if P8=="si":
            puntaje+=2
    P9=str(input("Trabajas?(si/no)\n")).lower()
    if P9=="si":
        puntaje+=20
    P10=str(input("Te gusta algun deporte?(si/no)\n")).lower()
    if P10=="si":
        puntaje+=10
    P11=str(input("Te gustan las series, peliculas o documentales?(si/no)\n")).lower()
    if P11=="si":
        puntaje+=10
    P12=str(input("Te gusta salir a pasear, comer, ir de compar? en general tener planes de salidas (si/no)\n")).lower()
    if P12=="si":
        puntaje+=10
    else:
        puntaje-=10
    P13=str(input("Te gustan los planes en casa?(si/no)\n")).lower()
    if P13=="si":
        puntaje+=30
    else:
        puntaje-=20
else:
    puntaje-=10000
    
print(f"Tu puntaje es de: {puntaje}")

if puntaje==160:
    print("Eres ideal")
elif 140<=puntaje<160:
    print("Estas muy bien")
elif 110<=puntaje<140:
    print("Estas bien")
elif 70<=puntaje<110:
    print("Estas mas o menos")
elif 40<=puntaje<70:
    print("Estas pasable")
else:
    print("Lo siento pero no")