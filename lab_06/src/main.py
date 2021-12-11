from color import base_color, red
from read_print import read_command, print_matrix
from full_combinations import parse_full_combinations
from generate import generate_file
from ant_algorythm import parse_ant_algorythm
from parametrization import parametrization
from compare_time import compare_time


def main():
    command = -1

    while command != 0:
        command = read_command()
        
        try:
            if command == 1:
                parse_full_combinations()

            elif command == 2:
                parse_ant_algorythm()

            elif command == 3:
                parametrization(True)

            elif command == 4:
                compare_time()

            elif command == 5:
                print_matrix()

            elif command == 6:
                generate_file()
        except:
            print("%s\nОшибка, ввод некорректные данных! %s"
                %(red, base_color))


if __name__ == "__main__":
    main()
