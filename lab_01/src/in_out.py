from color import set_color, base_color, yellow, red


MSG = "\n\t\t%s%sМеню\n\n"\
      "\t1. Расстояние Левенштейна (рекурсивная версия) \n"\
      "\t2. Расстояние Левенштейна (матричная версия) \n"\
      "\t3. Расстояние Дамерау-Левенштейна (рекурсивная версия) \n"\
      "\t4. Расстояние Дамерау-Левенштейна (матричная версия) \n"\
      "\t5. Замеры времени \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s%s"\
      %(set_color, yellow, set_color, base_color)


def input_command():
    try:
        command = int(input(MSG))
    except:
        command = -1
    
    if command < 0 or command > 5:
        print("%s%s\nОжидался ввод целого чилово числа от 0 до 5 %s%s"
            %(set_color, red, set_color, base_color))
        
    return command


def output_table(table, string_1, string_2):
    print("\n   ", end = " ")

    for i in string_2:
        print(i, end = " ")

    for i in range(len(table)):
        if i:
            print("\n" + string_1[i - 1], end = " ")
        else:
            print("\n ", end = " ")

        for j in range(len(table[i])):
            print(table[i][j], end = " ")

    print()
    