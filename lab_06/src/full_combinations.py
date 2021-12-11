import numpy as np
import itertools as it

from read_print import read_matrix
from color import base_color, purple 


def calc_length(matrix, size, way):
    length = 0

    for i in range(size):
        beg_city = way[i]
        end_city = way[i + 1]

        length += matrix[beg_city][end_city]

    return length


def full_combinations_alg(matrix, size):
    cities = np.arange(size)
    cities_combs = []

    for combination in it.permutations(cities):
        cities_combs.append(list(combination))

    best_way = []
    min_length = float("inf")

    for i in range(len(cities_combs)):
        cities_combs[i].append(cities_combs[i][0])

        length = calc_length(matrix, size, cities_combs[i])

        if length < min_length:
            min_length = length
            best_way = cities_combs[i]

    return min_length, best_way


def parse_full_combinations():
    matrix = read_matrix()
    size = len(matrix)

    min_length, best_way = full_combinations_alg(matrix, size)

    print("\n%sМинимальная сумма пути: %s" %(purple, base_color), min_length, 
          "\n%sМинимальный путь: %s" %(purple, base_color), best_way)
