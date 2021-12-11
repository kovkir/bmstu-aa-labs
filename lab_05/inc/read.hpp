#ifndef READ_HPP
#define READ_HPP

#include <iostream>
#include <stdio.h>

#include "errors.h"
#include "color.h"

#define MIN_COMMAND_NUMBER 0
#define MAX_COMMAND_NUMBER 3

void read_number_action(int &action);

void read_number_rows_columns(int &n, int &m);

void read_number_matrices(int &cnt);

#endif
