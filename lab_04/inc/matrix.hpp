#ifndef MATRIX_HPP
#define MATRIX_HPP

#include <iostream>

#include "errors.h"
#include "color.h"
#include "alloc_free_memory.hpp"

typedef struct matrix
{
    int **matrix;
    int n;
    int m;
} matrix_h;

void fill_matrix(matrix_h &matr);

void create_matrix(matrix_h &matr, int n, int m);

void print_matrix(matrix_h &matr);

#endif
