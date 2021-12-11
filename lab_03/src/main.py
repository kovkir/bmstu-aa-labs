from sorts import bubble_sort, select_sort, insertion_sort, sort
from color import set_color, base_color, red, yellow
from compare_time import compare_time


MSG = "\n\t\t%s%sМеню\n\n"\
      "\t1. Сортировка пузырьком \n"\
      "\t2. Сортировка выбором \n"\
      "\t3. Сортировка вставками \n"\
      "\t4. Замеры времени \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s%s"\
      %(set_color, yellow, set_color, base_color)


def input_option():
    try:
        option = int(input(MSG))
    except:
        option = -1
    
    if option < 0 or option > 4:
        print("%s%s\nОжидался ввод целого числа от 0 до 4 %s%s"
            %(set_color, red, set_color, base_color))

    return option


def main():
    option = -1

    while option != 0:
        option = input_option()

        if option == 1:
            sort(bubble_sort)

        elif option == 2:
            sort(select_sort)

        elif option == 3:
            sort(insertion_sort)

        elif option == 4:
            compare_time()


if __name__ == "__main__":
    main()
