#include "../inc/compare.hpp"
#include "../inc/matrix.hpp"
#include "../inc/sort.hpp"


void copy_matrix(matrix_h &old_matr, matrix_h &new_matr)
{
    for (int i = 0; i < old_matr.n; i++)
    {
        for (int j = 0; j < old_matr.m; j++)
        {
            new_matr.matrix[i][j] = old_matr.matrix[i][j];
        }
    }
}


double time_measurements(matrix_h &matr, int threads_count)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    matrix_h tmp_matr;
    double res_time = 0;

    for (int i = 0; i < NUMBER_RUNS; i++)
    {
        create_matrix(tmp_matr, matr.n, matr.m);
        copy_matrix(matr, tmp_matr);

        time_start = std::chrono::system_clock::now();
        select_sort_many_threads(tmp_matr, threads_count);
        time_end = std::chrono::system_clock::now();

        res_time += (std::chrono::duration_cast<std::chrono::nanoseconds>
                     (time_end - time_start).count());

        free_matrix(tmp_matr.matrix, tmp_matr.n);
    }

    res_time /= NUMBER_RUNS;

    return res_time / 1e9;
}


void compare_time(void)
{
    matrix_h matr;
    double time;

    for (int size = 100; size <= 200; size += 10)
    {
        create_matrix(matr, size, size);

        printf("%s\nСортировка матрицы размером %dx%d\n"
               "%s\n  Потоков |  Время \n"
                   "---------------------\n%s", 
                BLUE, matr.n, matr.m, GREEN, BASE_COLOR);

        for (int i = 1; i <= 32; i *= 2)
        {
            time = time_measurements(matr, i);
            printf("%6d    %s|%s %8f\n", i, GREEN, BASE_COLOR, time);
        }

        free_matrix(matr.matrix, matr.n);
    }
}
