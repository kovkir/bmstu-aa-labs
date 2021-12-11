import numpy as np
from random import randint

from color import base_color, green, blue


def generate_matrix(size, rand_start, rand_end):
    matrix = np.zeros((size, size), dtype = int)

    for i in range(size):
        for j in range(size):
            if (i == j):
                num = 0
            else:
                num = randint(rand_start, rand_end)

            matrix[i][j] = num
            matrix[j][i] = num

    return matrix


def generate_matrix_file(file_name, size, rand_start, rand_end):
    matrix = generate_matrix(size, rand_start, rand_end)
    file = open("../data/" + file_name, "w")

    for i in range(size):
        string = ""

        for j in range(size):
            string += str(matrix[i][j])
            string += " "

        string += "\n"
        file.write(string)

    file.close()

    return "\nФайл %s успешно создан\n" % (file_name)


def generate_file():
    file_name = input("\n%sВведите имя файла: %s" %(blue, base_color))
    size = int(input("%sВведите размер матрицы: %s" %(blue, base_color)))

    rand_start = int(input("\n%sВведите начальное число рандома: %s" %(blue, base_color)))
    rand_end   = int(input("%sВведите конечное число рандома: %s" %(blue, base_color)))

    print("%s" %(green) + generate_matrix_file(file_name, size, rand_start, rand_end) +
          "%s" %(base_color))
