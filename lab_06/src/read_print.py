from os import system
import numpy as np

from color import base_color, red, green, yellow, blue

MATRIX_SELECTION = False
KOEFS_INPUT      = False
DAYS_INPUT       = True

DEFAULT_MATRIX = 2
DEFAULT_ALPHA = 0.6
DEFAULT_EVAPORATION = 0.6
DEFAULT_DAYS = 20


MSG = "\n\t\t%sМеню\n\n"\
      "\t1. Полный перебор \n"\
      "\t2. Муравьиный алгоритм \n"\
      "\t3. Параметризация \n"\
      "\t4. Замеры времени \n"\
      "\t5. Распечатать матрицу \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s"\
      %(yellow, base_color)


def read_command():
    try:
        command = int(input(MSG))
    except:
        command = -1
    
    if command < 0 or command > 6:
        print("%s\nОжидался ввод целого числа от 0 до 5 %s"
            %(red, base_color))

    return command


def list_files():
    system("ls ../data > files.txt")

    f = open("files.txt", "r")
    files = f.read().split()
    f.close()

    if MATRIX_SELECTION:
        print("\n%sДоступные файлы: %s\n" %(green, base_color))

        for i in range(len(files)):
            print("    %2d. %s" % (i + 1, files[i]))

    system("rm files.txt")

    return files


def read_file_matrix(file_name):
    f = open("../data/" + file_name, "r")
    size = len(f.readline().split())
    f.seek(0)

    matrix = np.zeros((size, size), dtype = int)
    
    i = 0
    for line in f.readlines():
        j = 0

        for num in line.split():
            matrix[i][j] = int(num)
            j += 1

        i += 1

    f.close()

    return matrix


def read_matrix():
    files = list_files()

    if MATRIX_SELECTION:
        num_file = int(input("\n%sВыберите файл: %s" %(green, base_color))) - 1
    else:
        num_file = DEFAULT_MATRIX - 1

    matrix = read_file_matrix(files[num_file])

    return matrix


def print_matrix():
    files = list_files()

    if MATRIX_SELECTION:
        num_file = int(input("\n%sВыберите файл: %s" %(green, base_color))) - 1
    else:
        num_file = DEFAULT_MATRIX - 1
    
    matrix = read_file_matrix(files[num_file])

    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            print("%4d" % (matrix[i][j]), end = "")

        print()


def read_koefs():
    
    if KOEFS_INPUT:
        alpha       = float(input("\n%sВведите коэффициент alpha: %s" %(blue, base_color)))
        beta        = beta = 1 - alpha
        evaporation = float(input("%sВведите коэффициент evaporation: %s" %(blue, base_color)))
    else:
        alpha       = DEFAULT_ALPHA
        beta        = 1 - DEFAULT_ALPHA
        evaporation = DEFAULT_EVAPORATION

        print("\n%sКоэффициент alpha = %s%.1f"     %(blue, base_color, alpha))
        print("%sКоэффициент beta  = %s%.1f"       %(blue, base_color, beta))
        print("%sКоэффициент evaporation = %s%.1f" %(blue, base_color, evaporation))

    if DAYS_INPUT:
        days = int(input("\n%sВведите кол-во дней: %s" %(blue, base_color)))
    else:
        days = DEFAULT_DAYS
        print("%s\nКол-во дней = %s%d" %(blue, base_color, days))

    return alpha, beta, evaporation, days
