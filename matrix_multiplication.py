def criaMatrix(mat1, mat2):
    for a in range(3):
        mat1.append(0)
        mat1[a] = []
        for b in range(3):
            mat1[a].append(int(input(f'Digite um valor para [{a},{b}]: ')))
    for c in range(3):
        mat2.append(0)
        mat2[c] = []
        for d in range(3):
            mat2[c].append(int(input(f'Digite um valor para [{c},{d}]: ')))
    return mat1, mat2

def prodMatrix(mat1, mat2):
    mat3 = []
    for i in range(3):
        mat3.append([])
        for j in range(3):
            mat3[i].append(0)
            for k in range(3):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3

mat1 = []
mat2 = []
criaMatrix(mat1, mat2)
print(mat1)
print(mat2)
for i in range(3):
    for j in range(3):
        print(f'{prodMatrix(mat1, mat2)[i][j]:^5}', end=' ')
    print()
