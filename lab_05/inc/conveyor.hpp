#ifndef CONVEYOR_HPP
#define CONVEYOR_HPP

#include <iostream>
#include <queue>
#include <mutex>
#include <chrono>
#include <thread>

#include "errors.h"
#include "color.h"

#define THREADS_COUNT 3

struct result_time
{
    int task;
    int tape;

    double beg;
    double end;

    std::chrono::time_point<std::chrono::system_clock> time_begin;
};

using res_time_t = struct result_time;

void linear_processing(int n_matr, int m_matr, int cnt_matr, bool matr_is_print, bool compare_time);

void parallel_processing(int n_matr, int m_matr, int cnt_matr, bool matr_is_print, bool compare_time);

#endif
