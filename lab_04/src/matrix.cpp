#include "../inc/matrix.hpp"
#include "../inc/read.hpp"
#include "../inc/compare.hpp"

void fill_matrix(matrix_h &matr)
{
    for (int i = 0; i < matr.n; i++)
    {
        for (int j = 0; j < matr.m; j++)
        {
            matr.matrix[i][j] = rand() % 90 + 10;
        }
    }
}


void create_matrix(matrix_h &matr, int n, int m)
{   
    matr.n = n;
    matr.m = m;
    matr.matrix = allocate_matrix(n, m);

    if (!matr.matrix)
        throw memory_error(__FILE__, __LINE__);

    fill_matrix(matr);
}


void print_matrix(matrix_h &matr)
{
    std::cout << PURPLE << "\n";

    for (int i = 0; i < matr.n; i++)
    {
        for (int j = 0; j < matr.m; j++)
        {
            std::cout << matr.matrix[i][j] << " ";
        }
        std::cout << "\n";
    }

    std::cout << BASE_COLOR;
}
