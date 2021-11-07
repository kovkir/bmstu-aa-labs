#ifndef SORT_HPP
#define SORT_HPP

#include <iostream>

#include <thread>
#include <vector>

#include "errors.h"
#include "color.h"
#include "matrix.hpp"

void select_sort(int *arr, int n);

void select_sort_one_thread(matrix_h &matr);

void sort_part_matrix(matrix_h &matr, int numb_thread, int threads_count);

void select_sort_many_threads(matrix_h &matr, int threads_count);

#endif

