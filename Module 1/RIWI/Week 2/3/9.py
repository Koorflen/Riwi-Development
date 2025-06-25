P=input("Ingresa una palabra: ")
M=0
m=0

for letra in P:
    if letra.isupper():
        M+= 1
    elif letra.islower():
        m+= 1

print(f"Mayúsculas: {M}")
print(f"Minúsculas: {m}")