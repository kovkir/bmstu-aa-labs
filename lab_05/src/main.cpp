#include "../inc/main.hpp"

int main(void)
{   
    int n_matr, m_matr, cnt_matr, 
        action = -1;

    while (action)
    {
        try 
        {
            read_number_action(action);

            if (action == 1)
            {
                read_number_rows_columns(n_matr, m_matr);
                read_number_matrices(cnt_matr);

                linear_processing(n_matr, m_matr, cnt_matr, false, false);
            }
            else if (action == 2)
            {
                read_number_rows_columns(n_matr, m_matr);
                read_number_matrices(cnt_matr);

                parallel_processing(n_matr, m_matr, cnt_matr, false, false);
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


    return SUCCESS;
}
