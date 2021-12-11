#ifndef MATRIX_HPP
#define MATRIX_HPP

#include <iostream>
#include <vector>
#include <random>

#include "color.h"


struct matrix
{
    std::vector<std::vector<int>> matr;

    int n;
    int m;

    int min_elem;
    int sum_elem;
};

using matrix_t = struct matrix;

struct matrix_state
{
    bool stage_1;
    bool stage_2;
    bool stage_3;
};

using matrix_state_t = struct matrix_state;


matrix_t create_matrix(int n_matr, int m_matr);

matrix_t generate_matrix(int n_matr, int m_matr);

void print_matrix(matrix_t &matrix);

int get_min_elem(matrix_t &matrix);

void mod_by_min_elem(matrix_t &matrix);

int get_sum_elements(matrix_t &matrix);

void init_matrix_state_arr(std::vector<matrix_state_t> &matrix_state_arr, int cnt_matr);

#endif
