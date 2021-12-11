import numpy as np
from random import random

from read_print import read_matrix, read_koefs
from full_combinations import calc_length
from color import base_color, purple 

MIN_PHEROMONE = 0.01


def calc_q(matrix, size):
    q = 0
    count = 0

    for i in range(size):
        for j in range(size):
            if i != j:
                q += matrix[i][j]
                count += 1

    return q / count


def get_pherom_matr(size):
    pherom_matr = [[1 for i in range(size)] 
                        for j in range(size)]

    return pherom_matr


def get_visib_matr(matrix, size):
    visib_matr = [[(1.0 / matrix[i][j] if (i != j) else 0) 
                        for j in range(size)] 
                            for i in range(size)]

    return visib_matr


def get_visited_places(route, ants):
    visited_arr = [[] for _ in range(ants)]

    for i in range(ants):
        visited_arr[i].append(route[i])

    return visited_arr


def update_pherom_matr(matrix, size, visited_arr, pherom_matr, q, evaporation):
    ants = size

    for i in range(size):
        for j in range(size):
            delta = 0

            for ant in range(ants):
                length = calc_length(matrix, size, visited_arr[ant])
                delta += q / length

            pherom_matr[i][j] *= (1 - evaporation)
            pherom_matr[i][j] += delta

            if pherom_matr[i][j] < MIN_PHEROMONE:
               pherom_matr[i][j] = MIN_PHEROMONE

    return pherom_matr


def choose_next_place(pk):
    size = len(pk)
    numb = 0
    i = 0

    probability = random()

    while numb < probability and i < size:
        numb += pk[i]
        i += 1

    return i


def search_probability(pherom_matr, visib_matr, visited_arr, size, ant, alpha, beta):
    pk = [0] * size

    for i in range(size):
        if i not in visited_arr[ant]:
            ant_i = visited_arr[ant][-1]

            pk[i] = pow(pherom_matr[ant_i][i], alpha) * \
                    pow(visib_matr[ant_i][i],  beta)
        else:
            pk[i] = 0

    pk_sum = sum(pk)

    for i in range(size):
        pk[i] /= pk_sum  

    return pk


def ant_alg(matrix, size, alpha, beta, evaporation, days):
    pherom_matr = get_pherom_matr(size)
    visib_matr  = get_visib_matr(matrix, size)

    q = calc_q(matrix, size)

    best_way = []
    min_length = float("inf")

    for _ in range(days):
        visited_arr = get_visited_places(np.arange(size), size)

        for i in range(size):
            while len(visited_arr[i]) != size:
                pk = search_probability(pherom_matr, visib_matr, visited_arr, size, i, alpha, beta)  
                next_place = choose_next_place(pk)

                visited_arr[i].append(next_place - 1)

            visited_arr[i].append(visited_arr[i][0])
            
            length = calc_length(matrix, size, visited_arr[i]) 

            if length < min_length:
                min_length = length
                best_way = visited_arr[i]

        pherom_matr = update_pherom_matr(matrix, size, visited_arr, pherom_matr, q, evaporation)

    return min_length, best_way


def parse_ant_algorythm():
    matrix = read_matrix()
    size = len(matrix)
    
    alpha, beta, evaporation, days = read_koefs()
    min_length, best_way = ant_alg(matrix, size, alpha, beta, evaporation, days)

    print("\n%sМинимальная сумма пути: %s" %(purple, base_color), min_length, 
          "\n%sМинимальный путь: %s" %(purple, base_color), best_way)
    