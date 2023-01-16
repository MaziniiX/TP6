L1=[0]*3
L1[1]+=1
print(L1)
print(type(L1))
print("id de x: %d "%id(L1))
print()
for n in range(3):
    print("Execution n°",n)
    print("type =",type(L1[n]))
    print(L1[n])
    print("ID =%d"%id(L1[n]))
    print()