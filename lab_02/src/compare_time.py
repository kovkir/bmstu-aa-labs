from time import process_time
import matplotlib.pyplot as plt 

from matrix_mult import classical_alg, winograd_alg, optimized_winograd_alg
from color import set_color, base_color, purple

NUMB_RUNS = 1
COMPARE_TYPE = 0


def print_measurement_res(sizes, time_classical_alg, time_winograd_alg, time_optim_winograd_alg):

    print("\n%s%s  Размер | Стандартный алгоритм | Алгоритм Винограда | Оптим. алгоритм Винограда \n" 
                 "---------------------------------------------------------------------------------%s%s"
        %(set_color, purple, set_color, base_color))

    ind = 0

    for num in sizes:
        print("% 5d    %s%s|%s%s%15.2e       %s%s|%s%s%14.2e      %s%s|%s%s%17.2e " \
            %(num,                     set_color, purple, set_color, base_color, 
              time_classical_alg[ind], set_color, purple, set_color, base_color,
              time_winograd_alg[ind],  set_color, purple, set_color, base_color,
              time_optim_winograd_alg[ind]))

        ind += 1


def build_graph(sizes, time_classical_alg, time_winograd_alg, time_optim_winograd_alg):

    fig1 = plt.figure(figsize = (10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_classical_alg,      label = "Стандартный алгоритм")
    plot.plot(sizes, time_winograd_alg,       label = "Алгоритм Винограда")
    plot.plot(sizes, time_optim_winograd_alg, label = "Оптимизированный алгоритм Винограда")

    plt.legend()
    plt.grid()
    plt.title("Сравнение алгоритмом по времени")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размер (кол-во строк и столбцов)")
    
    plt.show()


def time_analysis(function, iterations, size):
    matr1 = [[0] * size for _ in range(size)]
    matr2 = [[0] * size for _ in range(size)]

    time_start = process_time()

    for _ in range(iterations):
        function(matr1, matr2)

    time_stop = process_time()

    return (time_stop - time_start) / iterations


def compare_time():
    time_classical_alg      = []
    time_winograd_alg       = []
    time_optim_winograd_alg = []

    if COMPARE_TYPE:
        sizes = [19, 29, 39, 49, 59, 69, 79, 89, 99]
        # sizes = [49, 99, 149, 199, 249, 299, 349]
    else:
        sizes = [20, 30, 40, 50, 60, 70, 80, 90, 100]
        # sizes = [50, 100, 150, 200, 250, 300, 350]
    
    for n in sizes:
        time_classical_alg.append(time_analysis(classical_alg, NUMB_RUNS, n))
        time_winograd_alg.append(time_analysis(winograd_alg, NUMB_RUNS, n))
        time_optim_winograd_alg.append(time_analysis(optimized_winograd_alg, NUMB_RUNS, n))

    print_measurement_res(sizes, time_classical_alg, time_winograd_alg, time_optim_winograd_alg)
    build_graph(sizes, time_classical_alg, time_winograd_alg, time_optim_winograd_alg)
