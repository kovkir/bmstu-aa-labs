#include "../inc/sort.hpp"


void select_sort(int *arr, int n)
{
    int min_j, tmp;
    
    for (int i = 0; i < n - 1; i++)
    {
        min_j = i;

        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_j])
            {
                min_j = j;
            }
        }

        if (min_j != i)
        {
            tmp = arr[i];
            arr[i] = arr[min_j];
            arr[min_j] = tmp;
        }
    }
}


void select_sort_one_thread(matrix_h &matr)
{
    for (int i = 0; i < matr.n; i++)
    {
        select_sort(matr.matrix[i], matr.m);
    }
}


void sort_part_matrix(matrix_h &matr, int numb_thread, int threads_count)
{
    for (int i = 0; i < matr.n; i++)
    {   
        if (i % threads_count == numb_thread)
            select_sort(matr.matrix[i], matr.m);
    }
}


void select_sort_many_threads(matrix_h &matr, int threads_count)
{   
    std::vector<std::thread> threads(threads_count);

    for (int i = 0; i < threads_count; i++)
    {
        threads[i] = std::thread(sort_part_matrix, std::ref(matr), i, threads_count);
    }

    for (int i = 0; i < threads_count; i++)
    {
        threads[i].join();
    }
}
