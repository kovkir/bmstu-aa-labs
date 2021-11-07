#include "../inc/alloc_free_memory.hpp"


void free_matrix(int **data, int n)
{
    for (int i = 0; i < n; i++)
        free(data[i]);

    free(data);
}


int **allocate_matrix(int n, int m)
{
    int **data = (int**) calloc(n, sizeof(int*));
 
    if (!data)
        return NULL;

    for (int i = 0; i < n; i++)
    {
        data[i] = (int*) calloc(m, sizeof(int));

        if (!data[i])
        {
            free_matrix(data, n);
            return NULL;
        }
    }

    return data;
}
