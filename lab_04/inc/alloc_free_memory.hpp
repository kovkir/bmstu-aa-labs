#ifndef ALLOC_FREE_MEMORY_H
#define ALLOC_FREE_MEMORY_H

#include <stdio.h>
#include <stdlib.h>

void free_matrix(int **data, int n);

int **allocate_matrix(int n, int m);

#endif
