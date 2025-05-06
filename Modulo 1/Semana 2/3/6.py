P=str(input("Ingresa una palabra\n")).lower()
C=0
for i in P:
    if i=="a":
        C+=1
print(f"La letra 'a' aparece {C} veces")