from color import set_color, base_color, red, blue

INPUT_TYPE = 0
FILE = "../docs/arr10.csv"

def input_arr_keyboard():
    arr = list()
    nums = 0

    print("%s%sВведите массив поэлементно в одной строке (окончание - Enter): %s%s"
        %(set_color, blue, set_color, base_color))

    nums = input().split()

    for i in range(len(nums)):
        try:
            arr.append(int(nums[i]))
        except:
            print("%s%s\nОшибка: введено не число%s%s"
                %(set_color, red, set_color, base_color))
            return []

    return arr


def input_arr_file():
    try:
        f = open(FILE, "r")
    except:
        print("%s%s\nОшибка: не удалось открыть файл%s%s\n"
            %(set_color, red, set_color, base_color))

        return input_arr_keyboard()

    arr = list()

    for line in f:
        try:
            arr.append(int(line))
        except:
            print("%s%s\nОшибка: введено не число%s%s"
                %(set_color, red, set_color, base_color))

    return arr


def input_arr():
    if INPUT_TYPE:
        arr = input_arr_keyboard()
    else:
        arr = input_arr_file()

    return arr
