mi_lista=[1,2,3,4,5]
L1=[10,20,30,40]
print(L1[0])
print(L1[-1])
L2=[10,20,30,40,50]
print(L2[1:4])
print(L2[:3])
print(L2[2:])
L1[2]=99
L3=[10,20,30]
L3.append(40)
L3.insert(1,15)
L3.extend([50,60])
L4=[10,20,30,40,50]
L4.remove(30)
L4.pop(-1)
del L4[1]
L5=[10,20,30,40,50]
print(20 in L5)
L5.index(30)
L5.count(20)
L6=[40,10,30,20]
print(sorted(L6))
print(sorted(L6, reverse=True))
L7=[10,20,30,40]
print(L7)
print(L7[::-1])
L7.reverse()
print(L7)
L8=[10,20,30]
print(L8[:])
print(list(L8))
print(L8.copy())
L9=[1,2,3,(4,3),"siete"]
if not L9:
    print("esta vacia")
else:
    print("tiene cosas")
L10=[]
N=int(input("Cuantos datos queires ingresar?\n"))
for i in range (N):
    W=input(f"ingresa el elemento {i+1}: ")
    L10.append(W)
print(L10)