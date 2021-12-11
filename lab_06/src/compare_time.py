from time import process_time
import matplotlib.pyplot as plt

from generate import generate_matrix
from ant_algorythm import ant_alg
from full_combinations import full_combinations_alg

from color import base_color, purple


def build_graph(sizes_arr, time_full_combinations, time_ant_algorythm):

    fig1 = plt.figure(figsize = (10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes_arr, time_full_combinations, label = "Алгоритм полного перебора")
    plot.plot(sizes_arr, time_ant_algorythm,     label = "Муравьиный алгоритм")

    plt.legend()
    plt.grid()
    plt.title("Измерение времени")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размер матрицы (эл)")
    
    plt.show()
    

def print_measurement_res(sizes_arr, time_full_combinations, time_ant_algorythm):

    print("\n%s  Размер |  Муравьиный алг. | полный перебор \n" 
            "---------------------------------------------%s"
        %(purple, base_color))

    ind = 0

    for num in sizes_arr:
        print("%6d   %s|%s   %12.4e   %s|%s  %12.4e " \
            %(num,                         purple, base_color, 
              time_full_combinations[ind], purple, base_color,
              time_ant_algorythm[ind]))

        ind += 1


def compare_time():
    time_full_combinations = []
    time_ant_algorythm = []

    sizes_arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    for size in sizes_arr:
        
        matrix = generate_matrix(size, 1, 2)

        start = process_time()
        full_combinations_alg(matrix, size)
        end = process_time()

        time_full_combinations.append(end - start)

        start = process_time()
        ant_alg(matrix, size, 0.5, 0.5, 0.5, 300)
        end = process_time()

        time_ant_algorythm.append(end - start)

    print_measurement_res(sizes_arr, time_full_combinations, time_ant_algorythm)
    build_graph(sizes_arr, time_full_combinations, time_ant_algorythm)
