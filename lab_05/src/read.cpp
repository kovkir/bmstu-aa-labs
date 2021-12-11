#include "../inc/read.hpp"


void read_number_action(int &action)
{   
    std::cout << YELLOW << 
            "\n\t\tМеню\n\n"
            "\t1. Линейная обработка\n"
            "\t2. Конвейерная обработка\n"
            "\t3. Замеры время\n"
            "\t0. Выход \n\n"
            "\tВыбор: " 
            << BASE_COLOR << "\n";

    int r = scanf("%d", &action);
    if (r != 1)
        throw no_number_entered_error(__FILE__, __LINE__);

    if (action < MIN_COMMAND_NUMBER || action > MAX_COMMAND_NUMBER)
        throw number_action_error(__FILE__, __LINE__);
}


void read_number_rows_columns(int &n, int &m)
{   
    std::cout << BLUE << "\nВведите кол-во строк матрицы: " << BASE_COLOR;

    int r = scanf("%d", &n);
    if (r != 1)
        throw no_number_entered_error(__FILE__, __LINE__);
        
    if (n <= 0)
        throw number_row_error(__FILE__, __LINE__);

    std::cout << BLUE << "Введите кол-во столбцов матрицы: " << BASE_COLOR;
    
    r = scanf("%d", &m);
    if (r != 1)
        throw no_number_entered_error(__FILE__, __LINE__);

    if (m <= 0)
        throw number_column_error(__FILE__, __LINE__);
}

void read_number_matrices(int &cnt)
{
     std::cout << GREEN << "\nВведите кол-во матриц: " << BASE_COLOR;

    int r = scanf("%d", &cnt);
    if (r != 1)
        throw no_number_entered_error(__FILE__, __LINE__);
        
    if (cnt <= 0)
        throw number_matrices_error(__FILE__, __LINE__);

    std::cout << "\n";
}
