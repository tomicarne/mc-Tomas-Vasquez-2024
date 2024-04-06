import math
z=0
while z<2 :
    x=input("1. vector \n2. matriz \n3.salir ")
    if x=="1":
        a = float(input("magnitud del primer vector"))
        b = float(input("magnitud del segundo vector"))
        c = float(input("angulo entre vectores"))
        resu1 = a*b*math.cos(c)
        print (resu1)
    elif x =="2":
        k1 = [[1,2,3],[7,32,54],[9,12,23],[3,6,1]]
        k2 = [[6,2,3],[9,32,54],[9,12,23],[3,6,13]]
        res1 = [[3 * el1 for el1 in row1] for row1 in k1]
        print("3 * primera matriz")
        for r1 in res1:
            print(r1)

        res2 = [[4 * el2 for el2 in row2] for row2 in k2]
        print("4 * segunda matriz")
        for r2 in res2:
            print(r2)
        res3= [[k1[i][j] + k2[i][j] for j in range(len(k1[i]))] for i in range(len(k1))]
        print("primera matriz + segunda matriz")
        for r3 in res3:
            print(r3)
        def mult(X,Y):
            res4 = [[sum(a*b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
            print("segunda matriz por primera matriz")
            for r4 in res4:
                print(r4)
        mult(k2,k1)
    elif x == "3":
        break
    else:
        print("numero no reconozido")
    


    