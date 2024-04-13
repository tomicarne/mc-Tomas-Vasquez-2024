def get_matrix_minor(m, row, col):
    return [[m[i][j] for j in range(len(m[i])) if j != col] for i in range(len(m)) if i != row]

def get_matrix_determinant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * get_matrix_determinant(get_matrix_minor(m, 0, c))
    return determinant

def get_matrix_inverse(m):
    determinant = get_matrix_determinant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactor_row = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactor_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = list(map(list, zip(*cofactors)))  # transpose
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

# define la primera matriz
A = [[3, 2, 2],
     [3, 1,-3],
     [1, 0,-2]]

B = [[1, 2, 0, 4],
     [2,0, -1,-2],
     [1,1, -1 ,0],
     [0,4 ,1 , 0]]

# calcular las matrices
A_inv = get_matrix_inverse(A)
B_inv = get_matrix_inverse(B)

# imprimir la matriz
print("la inversa de la matriz A =")
for row in A_inv:
    print(row)
print("inversa de la matriz b es")
for row1 in B_inv:
    print(row1)