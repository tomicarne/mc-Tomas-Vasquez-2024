import math

es=(0.5*(10**-8))*(100)

rad2=input("x en grados")
rad1 = math.radians(rad2)
ea = 100
aproxc = 1
ceka=1
sero =3
iteraciones=1


while ea>es:
    
    aproxn =  aproxc
    
    if ceka == 1:
        aproxc=aproxc-(rad1**sero)(math.factorial(sero))
    elif ceka==-1:
        aproxc=aproxc+(rad1**sero)(math.factorial(sero))
    

    ea=abs(((aproxc-aproxn)/aproxc)*100)

    sero+=2
    iteraciones += 1
    ceka *= -1


print("error aproximado",ea,"%")
print("error aproximado relativo porcentual",es,"%")
print("valor aproximada",aproxc)
print("numero de iteraciones:",iteraciones)