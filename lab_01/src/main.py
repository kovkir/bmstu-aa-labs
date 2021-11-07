from algorithms import lev_table, dam_lev_table, lev_recursion, dam_lev_recursion
from compare_time import compare_time
from in_out import input_command
from color import set_color, base_color, red, green, blue


def calc_distance(method):
    str_1 = input("\n%s%sВведите первую строку: %s%s" 
                %(set_color, blue, set_color, base_color))
    str_2 = input("%s%sВведите вторую строку: %s%s"
                %(set_color, blue, set_color, base_color))

    result = method(str_1, str_2, True)

    print("\n%s%sРасстояние = %s%s" 
        %(set_color, green, set_color, base_color), result)


def main():
    command = -1

    while command != 0:
        command = input_command()

        if command == 1:
            calc_distance(lev_recursion)

        elif command == 2:
            calc_distance(lev_table) 

        elif command == 3:
            calc_distance(dam_lev_recursion)

        elif command == 4:
            calc_distance(dam_lev_table)

        elif command == 5:
            compare_time()
        
            
if __name__ == "__main__": 
    main()