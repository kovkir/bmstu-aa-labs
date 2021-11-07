#include "../inc/main.hpp"

int main(void)
{   
    int action = -1, n, m;
    matrix_h matr;

    matr.matrix = nullptr;
    matr.n = 0;
    matr.m = 0;

    while (action)
    {
        try 
        {
            read_number_action(action);

            if (action == 1)
            {
                read_number_rows_columns(n, m);
                free_matrix(matr.matrix, matr.n);
                create_matrix(matr, n, m);

                std::cout << GREEN << "\nЗаполненная рандомными числами матрица:\n" << BASE_COLOR;
                print_matrix(matr);

                select_sort_one_thread(matr);
                std::cout << GREEN << "\nМатрица с отсортированными строками:\n" << BASE_COLOR;
                print_matrix(matr);
            }
            else if (action == 2)
            {
                read_number_rows_columns(n, m);
                free_matrix(matr.matrix, matr.n);
                create_matrix(matr, n, m);
                
                std::cout << GREEN << "\nЗаполненная рандомными числами матрица:\n" << BASE_COLOR;
                print_matrix(matr);

                select_sort_many_threads(matr, THREADS_COUNT);
                std::cout << GREEN << "\nМатрица с отсортированными строками:\n" << BASE_COLOR;
                print_matrix(matr);
            }
            else if (action == 3)
            {
                compare_time();
            }
        }
        catch (base_error &error)
        {
            std::cout << RED << error.what() << BASE_COLOR << std::endl;
            fflush(stdin);
        }
    }

    free_matrix(matr.matrix, matr.n);

    return SUCCESS;
}
