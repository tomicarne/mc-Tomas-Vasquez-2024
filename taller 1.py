cantidad_a=int(input("numero de elementos A"))
cantidad_b=int(input("numero de elementos B"))

elementA = set()
elementB = set()
elementC = set()
for i in range(cantidad_a):
    elemento = int(input("elemento numero "))
    elementA.add(elemento)

for i in range(cantidad_b):
    element = int(input("elemento numero "))
    elementB.add(element)

print(elementA)
print(elementB)

des = int(input("escriba el numero de la operacion que desea \n 1. union \n 2.interseccion \n 3.diferencia \n 4.diferencia simetrica \n 5.ninguna operacion"))
if des == 1:
    elementC = elementA.union(elementB)
elif des == 2:
    elementC = elementA.interseccion(elementB)
elif des == 3:
    elementC = elementA.diferencia(elementB)
elif des == 4:
    elementC = elementA ^ elementB
elif des == 5:
    print("eligio ninguna operacion")
else:
    print("operacion incorrecta")



print(elementC)