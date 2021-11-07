from in_out_matrix import input_matrix, print_matrix, INPUT_TYPE
from color import set_color, base_color, purple, red

def matrix_mult(method):

    print("%s%s\n\tМатрица 1%s%s"
        %(set_color, purple, set_color, base_color))

    matr1 = input_matrix()
    if matr1 == []:
        return

    if INPUT_TYPE:
        print_matrix(matr1)

    print("%s%s\n\tМатрица 2%s%s"
        %(set_color, purple, set_color, base_color))

    matr2 = input_matrix()
    if matr2 == []:
        return
    
    if INPUT_TYPE:
        print_matrix(matr2)

    if len(matr2) != len(matr1[0]):
        print("%s%s\n\tКол-во столбцов первой матрицы должно ровняться кол-ву строк второй матрицы!%s%s"
            %(set_color, red, set_color, base_color))
        return

    res = method(matr1, matr2)

    print("%s%s\n\tРезультат умножения матриц%s%s"
        %(set_color, purple, set_color, base_color))

    print_matrix(res)


def classical_alg(matr1, matr2):

    n = len(matr1)
    m = len(matr1[0])
    k = len(matr2[0])

    res_matr = [[0] * k for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for u in range(m):
                res_matr[i][j] += matr1[i][u] * matr2[u][j]

    return res_matr


def winograd_alg(matr1, matr2):

    n = len(matr1)
    m = len(matr1[0])
    k = len(matr2[0])

    res_matr = [[0] * k for _ in range(n)]

    tmp_r = [0] * n
    for i in range(n):
        for j in range(0, m // 2, 1):
            tmp_r[i] += matr1[i][2 * j] * matr1[i][2 * j + 1]

    tpm_c = [0] * k
    for i in range(k):
        for j in range(0, m // 2, 1):
            tpm_c[i] += matr2[2 * j][i] * matr2[2 * j + 1][i]

    for i in range(n):
        for j in range(k):
            res_matr[i][j] = -tmp_r[i] - tpm_c[j]

            for u in range(0, m // 2, 1):
                res_matr[i][j] += (matr1[i][2 * u + 1] + matr2[2 * u    ][j]) * \
                                  (matr1[i][2 * u    ] + matr2[2 * u + 1][j])

    if m % 2 == 1:
        for i in range(n):
            for j in range(k):
                res_matr[i][j] += matr1[i][m - 1] * matr2[m - 1][j]

    return res_matr


def optimized_winograd_alg(matr1, matr2):

    n = len(matr1)
    m = len(matr1[0])
    k = len(matr2[0])

    res_matr = [[0] * k for _ in range(n)]

    tmp_r = [0] * n
    for i in range(n):
        for j in range(1, m, 2):
            tmp_r[i] += matr1[i][j] * matr1[i][j - 1]

    tpm_c = [0] * k
    for i in range(k):
        for j in range(1, m, 2):
            tpm_c[i] += matr2[j][i] * matr2[j - 1][i]

    flag = n % 2
    for i in range(n):
        for j in range(k):
            res_matr[i][j] = -(tmp_r[i] + tpm_c[j])

            for u in range(1, m, 2):
                res_matr[i][j] += (matr1[i][u - 1] + matr2[u    ][j]) * \
                                  (matr1[i][u    ] + matr2[u - 1][j])
            if flag:
                res_matr[i][j] += matr1[i][m - 1] * matr2[m - 1][j]

    return res_matr
    