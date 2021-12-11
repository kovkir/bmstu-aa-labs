#include "../inc/matrix.hpp"

matrix_t create_matrix(int n_matr, int m_matr)
{
    matrix_t matrix;

    matrix.n = n_matr;
    matrix.m = m_matr;
    matrix.matr.resize(n_matr);

    for (int i = 0; i < n_matr; i++)
    {
        matrix.matr[i].resize(m_matr);
    }

    return matrix;
}


matrix_t generate_matrix(int n_matr, int m_matr)
{
    matrix_t matrix = create_matrix(n_matr, m_matr);
    
    for (int i = 0; i < matrix.n; i++)
    {
        for (int j = 0; j < matrix.m; j++)
        {
            matrix.matr[i][j] = rand() % 90 + 10;
        }
    }

    return matrix;
}


void print_matrix(matrix_t &matrix)
{
    std::cout << PURPLE << "\n";

    for (int i = 0; i < matrix.n; i++)
    {
        for (int j = 0; j < matrix.m; j++)
        {
            std::cout << matrix.matr[i][j] << " ";
        }
        std::cout << "\n";
    }

    std::cout << BASE_COLOR;
}


int get_min_elem(matrix_t &matrix)
{
    int min_elem = matrix.matr[0][0];

    for (int i = 0; i < matrix.n; i++)
    {
        for (int j = 0; j < matrix.m; j++)
        {
            if (matrix.matr[i][j] < min_elem)
            {
                min_elem = matrix.matr[i][j];
            }
        }
    }

    return min_elem;
}


void mod_by_min_elem(matrix_t &matrix)
{   
    for (int i = 0; i < matrix.n; i++)
    {
        for (int j = 0; j < matrix.m; j++)
        {
            matrix.matr[i][j] %= matrix.min_elem;
        }
    }
}


int get_sum_elements(matrix_t &matrix)
{
    int sum = 0;

    for (int i = 0; i < matrix.n; i++)
    {
        for (int j = 0; j < matrix.m; j++)
        {
            sum += matrix.matr[i][j];
        }
    }

    return sum;
}


void init_matrix_state_arr(std::vector<matrix_state_t> &matrix_state_arr, int cnt_matr)
{
    matrix_state_arr.resize(cnt_matr);

    for (int i = 0; i < cnt_matr; i++)
    {
        matrix_state_t matr_state;

        matr_state.stage_1 = false;
        matr_state.stage_2 = false;
        matr_state.stage_3 = false;

        matrix_state_arr[i] = matr_state;
    }
}
