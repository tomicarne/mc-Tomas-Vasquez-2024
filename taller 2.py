cantidad_u=int(input("numero de elementos universales"))
cantidad_b=int(input("numero de elementos A"))

elementu = set()
elementB = set()
elementC = set()
elementD = set()
elementE = set()
for i in range(cantidad_u):
    elemento = int(input("elemento conjunto universal numero"))
    elementu.add(elemento)

for i in range(cantidad_b):
    element = int(input("elemento conjunto A numero"))
    elementB.add(element)

print("elemento u", elementu)
print("elemento a", elementB)

if elementu >= elementB:
    elementC = (elementu|elementB)&elementB
    elementD = (elementu&elementB)^elementB
    elementE = (elementu-elementB)^elementB
    print(elementC)
    print(elementD)
    print(elementE)
else:
    SystemExit
