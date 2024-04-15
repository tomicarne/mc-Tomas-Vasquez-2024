import matplotlib.pyplot as plt

# (x) y (y)
X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [9, 7, 8, 5, 6, 4.5 , 4 , 2.5]
#X = [1, 2, 3, 4, 5, 6, 7]
#Y = [0.5, 2.5, 2, 4, 3.5, 6, 5.5]

# calcualdora de promedio
X_mean = sum(X) / len(X)
Y_mean = sum(Y) / len(Y)

# calcula a sub 1 y 0
suma_x = suma_y = suma_xy = suma_x2 = 0
for r in range(len(X)):
    suma_x = suma_x + X[r]
    suma_y = suma_y + Y[r]
    suma_xy = suma_xy + X[r] * Y[r]
    suma_x2 = suma_x2 + X[r]**2

print(suma_x, suma_y, suma_xy, suma_x2)

a1 = (len(X)*suma_xy-suma_x*suma_y)/(len(X)*suma_x2-suma_x**2)
a0 = Y_mean-(a1*X_mean)
# imprime
print("a sub zero", a0)
print("a sub 1:", a1)

# graficar??
plt.scatter(X, Y)
plt.plot([min(X), max(X)], [a0 + a1*min(X), a0 + a1*max(X)])
plt.show()