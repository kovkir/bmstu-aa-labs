import matplotlib.pyplot as plt 
import numpy as np
from color import base_color, red, yellow


MSG = "\n\t\t%sМеню\n\n"\
      "\t1. Построить граф зависимости времени от кол-ва матриц \n"\
      "\t2. Построить граф зависмости времени от размера матриц \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s"\
      %(yellow, base_color)


def build_graph_different_quantities():

    quantities = [50, 100, 200, 400, 800, 1600]

    time_parallel_proc = [0.008400, 0.012959, 0.033233, 0.042608, 0.083202, 0.157260]
    time_linear_proc   = [0.015424, 0.027467, 0.054710, 0.107318, 0.216504, 0.421379]

    fig1 = plt.figure(figsize = (9, 6))
    plot = fig1.add_subplot()
    plot.plot(quantities, time_parallel_proc, label = "Конвейерная обработка")
    plot.plot(quantities, time_linear_proc,   label = "Линейная обработка")

    plt.legend()
    plt.grid()
    plt.title("Зависимость времени обработки от кол-ва матриц\n "
              "(размеры матриц 100х100)")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Кол-во матриц (шт)")
    plt.xticks(np.arange(0, 1601, 200))
    
    plt.show()


def build_graph_different_sizes():
    
    quantities = [20, 40, 80, 160, 320, 640]

    time_parallel_proc = [0.001169, 0.003011, 0.007220, 0.022288, 0.081844, 0.310014]
    time_linear_proc   = [0.003016, 0.007714, 0.018300, 0.061450, 0.235350, 0.899033]

    fig1 = plt.figure(figsize = (9, 6))
    plot = fig1.add_subplot()
    plot.plot(quantities, time_parallel_proc, label = "Конвейерная обработка")
    plot.plot(quantities, time_linear_proc,   label = "Линейная обработка")

    plt.legend()
    plt.grid()
    plt.title("Зависимость времени обработки от размеров матриц\n "
              "(кол-во матриц = 100)")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размеры матриц (эл)")
    plt.xticks(np.arange(0, 641, 80))
    
    plt.show()


def input_option():
    try:
        option = int(input(MSG))
    except:
        option = -1
    
    if option < 0 or option > 2:
        print("%s\nОжидался ввод целого чилово числа от 0 до 2 %s"
            %(red, base_color))

    return option


def main():
    option = -1

    while option != 0:
        option = input_option()

        if option == 1:
            build_graph_different_quantities()

        elif option == 2:
            build_graph_different_sizes()


if __name__ == "__main__":
    main()
