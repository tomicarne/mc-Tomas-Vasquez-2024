import math

es=(0.5*(10**-8))*(100)

rad1=-0,75
ea = 100
aproxc = 1
ceka=1
sero =1
iteraciones=1
i = input("1. e**-x   2.   1/(e**x)")


while ea>es:
    
    aproxn =  aproxc
    if i == 1:
        if ceka == 1:
            aproxc=aproxc-(rad1**sero)(math.factorial(sero))
        elif ceka==-1:
            aproxc=aproxc+(rad1**sero)(math.factorial(sero))
    elif i==2:
        aproxc=1/(aproxc-(rad1**sero)(math.factorial(sero)))
    else:
        print("unknown input")

    ea=abs(((aproxc-aproxn)/aproxc)*100)

    sero+=1
    iteraciones += 1
    ceka *= -1


print("error aproximado",ea,"%")
print("error aproximado relativo porcentual",es,"%")
print("valor aproximada",aproxc)
print("numero de iteraciones:",iteraciones)