N=int(input("Ingrese un numero\n"))
if N%3==0:
    if N%5==0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif N%5==0:
    print("Buzz")
else:
    print("Nada Magico")