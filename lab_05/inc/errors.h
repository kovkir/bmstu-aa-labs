#ifndef ERRORS_H
#define ERRORS_H

#include <exception>
#include <string>

#define SUCCESS 0


class base_error : public std::exception
{
public:
    base_error(
        std::string filename, 
        int line, 
        std::string info = "Ошибка!")
    {
        err_info = "\nFile name: " + filename + 
                   "\nLine: " + std::to_string(line) +
                   "\nInfo: " + info;
    }

    virtual const char* what() const noexcept override
    {
        return err_info.c_str();
    }

protected:
    std::string err_info;
};


class number_action_error : public base_error
{
public:
    number_action_error(
        std::string filename, 
        int line, 
        std::string info = "Такого номера команды нет!\n") :

    base_error(filename, line, info) {};
};


class number_row_error : public base_error
{
public:
    number_row_error(
        std::string filename, 
        int line, 
        std::string info = "Кол-во строк должно быть > 0!\n") :

    base_error(filename, line, info) {};
};


class number_column_error : public base_error
{
public:
    number_column_error(
        std::string filename, 
        int line, 
        std::string info = "Кол-во столбцов должно быть > 0!\n") :

    base_error(filename, line, info) {};
};


class number_matrices_error : public base_error
{
public:
    number_matrices_error(
        std::string filename, 
        int line, 
        std::string info = "Кол-во матриц должно быть > 0!\n") :

    base_error(filename, line, info) {};
};


class no_number_entered_error : public base_error
{
public:
    no_number_entered_error(
        std::string filename, 
        int line, 
        std::string info = "Ожидался ввод целово числа!\n") :

    base_error(filename, line, info) {};
};

#endif
