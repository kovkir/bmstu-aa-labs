from color import set_color, base_color, purple, red, blue, green

INPUT_TYPE = 0


def print_matrix(matr):
    n = len(matr)
    m = len(matr[0])

    print()
    for i in range (n):
        for j in range (m):
            print("%s%s%4d%s%s" 
            %(set_color, base_color, matr[i][j], set_color, base_color), end = '')
        print()


def input_matrix_keyboard():
    try:
        n = int(input("\n%s%sВведите количество строк: %s%s"
                    %(set_color, blue, set_color, base_color)))

        if n < 1:
            print("%s%s\nКол-во строк матрицы должно быть больше 0!%s%s"
                %(set_color, red, set_color, base_color))
            return []

        m = int(input("%s%sВведите количество столбцов: %s%s"
                    %(set_color, blue, set_color, base_color)))

        if m < 1:
            print("%s%s\nКол-во столбцов матрицы должно быть больше 0!%s%s"
                %(set_color, red, set_color, base_color))
            return []

    except:
        print("%s%s\nКол-во строк и столбцов матрицы - целые числа!%s%s"
                %(set_color, red, set_color, base_color))
        return []

    print("%s%s\nЗаполните матрицу, разделяя элементы одной строки пробелом:\n%s%s"
        %(set_color, green, set_color, base_color))

    matr = []

    for i in range(n):
        try:
            arr = list(int(i) for i in input().split())
        except:
            print("\n%s%sМатрица должна содержать только целые числа!%s%s"
                %(set_color, red, set_color, base_color))
            return []
        
        if len(arr) != m:
            print("\n%s%sНеверное кол-во столбцов в матрице!%s%s"
                %(set_color, red, set_color, base_color))
            return []
        else:
            matr.append(arr)

    return matr


def input_matrix():
    if INPUT_TYPE:
        matr = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    else:
        matr = input_matrix_keyboard()
        
    return matr
