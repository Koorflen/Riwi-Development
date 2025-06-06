matriz=[]

sub=[]

for i in range (3):
    for j in range(1):
        sub.append(j+1)
    matriz.append(sub)
    
for i in matriz:
    print(i)