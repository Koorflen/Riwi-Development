P=str(input("Ingresa una palabra\n"))
L=""
R=0
for i in P:
    C=0
    for c in P:
        if i==c:
            C+=1
    if C>R:
        R=C
        L=i
print(f"La letra mas repetida es {L} (aparece {R} veces)")