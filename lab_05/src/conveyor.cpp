#include "../inc/conveyor.hpp"
#include "../inc/matrix.hpp"


void print_res_time(std::vector<res_time_t> &time_result_arr, int size_arr)
{
    printf("%s--------------------------------------------------------%s"
           "\n  № Матрицы  %s|%s   № Этапа  %s|%s Время начала %s|%s Время конца \n"
           "%s--------------------------------------------------------\n%s",
            PURPLE, BASE_COLOR, PURPLE, BASE_COLOR, PURPLE, BASE_COLOR,
            PURPLE, BASE_COLOR, PURPLE, BASE_COLOR); 

    for (int i = 0; i < size_arr; i++)
    {
        printf("    %3d      %s|%s     %2d     %s|%s   %.6f   %s|%s   %.6f   \n", 
                time_result_arr[i].task, PURPLE, BASE_COLOR,
                time_result_arr[i].tape, PURPLE, BASE_COLOR,
                time_result_arr[i].beg,  PURPLE, BASE_COLOR,
                time_result_arr[i].end);
        
        if ((i + 1) % 3 == 0)
        {
            printf("%s--------------------------------------------------------\n%s", 
                    PURPLE, BASE_COLOR);
        }
    }
}


void init_time_result_arr(std::vector<res_time_t> &time_result_arr, 
                          std::chrono::time_point<std::chrono::system_clock> time_begin,
                          int cnt_matr, int cnt_threads)
{
    int len = cnt_matr * cnt_threads;
    time_result_arr.resize(len);

    for (int i = 0; i < len; i++)
    {
        res_time_t time_res;
        time_res.time_begin = time_begin;

        time_result_arr[i] = time_res;
    }

}


void save_result(std::vector<res_time_t> &time_result_arr, 
                 std::chrono::time_point<std::chrono::system_clock> time_start,
                 std::chrono::time_point<std::chrono::system_clock> time_end,
                 std::chrono::time_point<std::chrono::system_clock> time_begin,
                 int task_num, int numb_stage)
{
    double beg_time = (std::chrono::duration_cast<std::chrono::nanoseconds> 
                    (time_start - time_begin).count()) / 1e9;

    double end_time = (std::chrono::duration_cast<std::chrono::nanoseconds> 
                    (time_end - time_begin).count()) / 1e9;

    int index = (task_num - 1) * THREADS_COUNT + numb_stage - 1;

    time_result_arr[index].task = task_num;
    time_result_arr[index].tape = numb_stage;
    time_result_arr[index].beg = beg_time;
    time_result_arr[index].end = end_time;
}


void stage_1(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2)
{
    std::mutex m;

    m.lock();
    matrix_t matr = q1.front();
    m.unlock();

    matr.min_elem = get_min_elem(matr);

    m.lock();
    q2.push(matr);
    m.unlock();

    m.lock();
    q1.pop();
    m.unlock();
}


void stage_2(std::queue<matrix_t> &q2, std::queue<matrix_t> &q3)
{
    std::mutex m;

    m.lock();
    matrix_t matr = q2.front();
    m.unlock();

    mod_by_min_elem(matr);
    
    m.lock();
    q3.push(matr);
    m.unlock();
    
    m.lock();
    q2.pop();
    m.unlock();
}


void stage_3(std::queue<matrix_t> &q3, int task_num, int cnt_matr, bool matr_is_print)
{
    std::mutex m;

    m.lock();
    matrix_t matr = q3.front();
    m.unlock();

    matr.sum_elem = get_sum_elements(matr);
    
    if (matr_is_print && task_num == cnt_matr)
    {
        printf("\nmin_elem = %d\n\nМатрица после 2 этапа:\n", matr.min_elem);        
        print_matrix(matr);
        printf("\nsum_elem = %d\n\n", matr.sum_elem);
    }

    m.lock();
    q3.pop();
    m.unlock();
}


void linear_processing(int n_matr, int m_matr, int cnt_matr, bool matr_is_print, bool compare_time)
{
    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    std::mutex m;

    for (int i = 0; i < cnt_matr; i++)
    {
        matrix_t matr = generate_matrix(n_matr, m_matr);
        q1.push(matr);

        if (matr_is_print && i == cnt_matr - 1)
        {
            m.lock();
            printf("Первоначальная матрица:\n");
            print_matrix(matr);
            m.unlock();
        }
    }

    std::vector<matrix_state_t> matrix_state_arr;
    init_matrix_state_arr(matrix_state_arr, cnt_matr);

    std::chrono::time_point<std::chrono::system_clock> time_start, time_end, 
    time_begin = std::chrono::system_clock::now();

    std::vector<res_time_t> time_result_arr;
    init_time_result_arr(time_result_arr, time_begin, cnt_matr, THREADS_COUNT);

    for (int i = 0; i < cnt_matr; i++)
    {
        time_start = std::chrono::system_clock::now();
        stage_1(std::ref(q1), std::ref(q2));
        time_end = std::chrono::system_clock::now();
        
        save_result(time_result_arr, time_start, time_end, time_begin, i + 1, 1);

        time_start = std::chrono::system_clock::now();
        stage_2(std::ref(q2), std::ref(q3));
        time_end = std::chrono::system_clock::now();

        save_result(time_result_arr, time_start, time_end, time_begin, i + 1, 2);

        time_start = std::chrono::system_clock::now();
        stage_3(std::ref(q3), i + 1, cnt_matr, matr_is_print);
        time_end = std::chrono::system_clock::now();

        save_result(time_result_arr, time_start, time_end, time_begin, i + 1, 3);
    }

    if (compare_time)
    {
        printf("     %4d      %s|%s     %4d      %s|%s   %.6f  \n",
            n_matr, PURPLE, BASE_COLOR, 
            cnt_matr, PURPLE, BASE_COLOR,
            time_result_arr[cnt_matr - 1].end);
    }
    else
    {
        print_res_time(time_result_arr, cnt_matr * THREADS_COUNT);
    }
}


void parallel_stage_1(std::queue<matrix_t> &q1, std::queue<matrix_t> &q2,
                      std::vector<res_time_t> &time_result_arr,
                      std::vector<matrix_state_t> &matrix_state_arr, 
                      bool &q1_is_empty)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    int task_num = 1;

    while(!q1.empty())
    {   
        time_start = std::chrono::system_clock::now();
        stage_1(std::ref(q1), std::ref(q2));
        time_end = std::chrono::system_clock::now();

        save_result(time_result_arr, time_start, time_end, time_result_arr[0].time_begin, task_num, 1);

        matrix_state_arr[task_num - 1].stage_1 = true;
        task_num++;
    }

    q1_is_empty = true;
}


void parallel_stage_2(std::queue<matrix_t> &q2, std::queue<matrix_t> &q3,
                      std::vector<res_time_t> &time_result_arr,
                      std::vector<matrix_state_t> &matrix_state_arr, 
                      bool &q1_is_empty, bool &q2_is_empty)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    int task_num = 1;

    while(true)
    {      
        if (!q2.empty())
        {   
            if (matrix_state_arr[task_num - 1].stage_1 == true)
            {
                time_start = std::chrono::system_clock::now();
                stage_2(std::ref(q2), std::ref(q3));
                time_end = std::chrono::system_clock::now();

                save_result(time_result_arr, time_start, time_end, time_result_arr[0].time_begin, task_num, 2);

                matrix_state_arr[task_num - 1].stage_2 = true;
                task_num++;
            }
        }
        else if(q1_is_empty)
        {
            break;
        }
    }

    q2_is_empty = true;
}


void parallel_stage_3(std::queue<matrix_t> &q3, 
                      std::vector<res_time_t> &time_result_arr,
                      std::vector<matrix_state_t> &matrix_state_arr, 
                      bool &q2_is_empty, int cnt_matr, bool matr_is_print)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    int task_num = 1;

    while(true)
    {      
        if (!q3.empty())
        {   
            if (matrix_state_arr[task_num - 1].stage_2 == true)
            {
                time_start = std::chrono::system_clock::now();
                stage_3(std::ref(q3), task_num, cnt_matr, matr_is_print);
                time_end = std::chrono::system_clock::now();

                save_result(time_result_arr, time_start, time_end, time_result_arr[0].time_begin, task_num, 3);

                matrix_state_arr[task_num - 1].stage_3 = true;
                task_num++;
            }
        }
        else if(q2_is_empty)
        {
            break;
        } 
    }
}


void parallel_processing(int n_matr, int m_matr, int cnt_matr, bool matr_is_print, bool compare_time)
{
    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    std::mutex m;

    for (int i = 0; i < cnt_matr; i++)
    {
        matrix_t matr = generate_matrix(n_matr, m_matr);
        q1.push(matr);

        if (matr_is_print && i == cnt_matr - 1)
        {
            m.lock();
            printf("Первоначальная матрица:\n");
            print_matrix(matr);
            m.unlock();
        }
    }
    
    bool q1_is_empty = false;
    bool q2_is_empty = false;

    std::vector<matrix_state_t> matrix_state_arr;
    init_matrix_state_arr(matrix_state_arr, cnt_matr);

    std::chrono::time_point<std::chrono::system_clock> time_begin = 
    std::chrono::system_clock::now();

    std::vector<res_time_t> time_result_arr;
    init_time_result_arr(time_result_arr, time_begin, cnt_matr, THREADS_COUNT);

    std::thread threads[THREADS_COUNT];

    threads[0] = std::thread(parallel_stage_1, std::ref(q1), std::ref(q2), std::ref(time_result_arr), std::ref(matrix_state_arr), std::ref(q1_is_empty));
    threads[1] = std::thread(parallel_stage_2, std::ref(q2), std::ref(q3), std::ref(time_result_arr), std::ref(matrix_state_arr), std::ref(q1_is_empty), std::ref(q2_is_empty));
    threads[2] = std::thread(parallel_stage_3, std::ref(q3), std::ref(time_result_arr), std::ref(matrix_state_arr), std::ref(q2_is_empty), cnt_matr, matr_is_print);

    for (int i = 0; i < THREADS_COUNT; i++)
    {
        threads[i].join();
    }

    if (compare_time)
    {
        printf("     %4d      %s|%s     %4d      %s|%s   %.6f  \n",
            n_matr, PURPLE, BASE_COLOR, 
            cnt_matr, PURPLE, BASE_COLOR,
            time_result_arr[cnt_matr - 1].end);
    }
    else
    {
        print_res_time(time_result_arr, cnt_matr * THREADS_COUNT);
    }
}
