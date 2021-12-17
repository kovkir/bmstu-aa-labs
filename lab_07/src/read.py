from color import *
from alg_search import *
from dictionary import sort_dict_by_key, segment_dict


MSG = "\n\t\t%sМеню\n\n"\
      "\t1. Полный перебор \n"\
      "\t2. Бинарный поиск \n"\
      "\t3. Поиск сегментами \n"\
      "\t4. Замеры времени \n"\
      "\t5. Провести анализ кол-ва сравнений \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s"\
      %(yellow, base_color)

ALG = "\n\t\t%sВыбор алгоритма\n\n"\
      "\t1. Полный перебор \n"\
      "\t2. Бинарный поиск \n"\
      "\t3. Поиск сегментами \n\n"\
      "\tВыбор: %s"\
      %(blue, base_color)


def read_command():
    try:
        command = int(input(MSG))
    except:
        command = -1
    
    if command < 0 or command > 5:
        print("%s\nОжидался ввод целого числа от 0 до 5 %s"
            %(red, base_color))

    return command


def read_alg(dictionary):
    try:
        command = int(input(ALG))
    except:
        command = -1

    if command == 1:
        return full_search, "Полный перебор", dictionary

    elif command == 2:
        return binary_search, "Бинарный поиск", sort_dict_by_key(dictionary)
        
    elif command == 3:
        return segment_search, "Поиск сегментами", segment_dict(sort_dict_by_key(dictionary))

    else:
        print("%s\nОжидался ввод целого числа от 0 до 3 %s" %(red, base_color))

