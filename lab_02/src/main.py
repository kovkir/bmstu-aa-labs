from matrix_mult import classical_alg, winograd_alg, optimized_winograd_alg, matrix_mult
from compare_time import compare_time
from color import set_color, base_color, yellow, red


MSG = "\n\t\t%s%sМеню\n\n"\
      "\t1. Умножение матриц классическим алгоритмом \n"\
      "\t2. Умножение матриц алгоритмом Винограда \n"\
      "\t3. Умножение матриц оптимизированным алгоритмом Винограда\n"\
      "\t4. Замеры времени \n"\
      "\t0. Выход \n\n"\
      "\tВыбор: %s%s"\
      %(set_color, yellow, set_color, base_color)


def input_command():
    try:
        command = int(input(MSG))
    except:
        command = -1
    
    if command < 0 or command > 4:
        print("%s%s\nОжидался ввод целого чилово числа от 0 до 4 %s%s"
             %(set_color, red, set_color, base_color))

    return command
        

def main():
    command = -1

    while command != 0:
        command = input_command()

        if command == 1:
            matrix_mult(classical_alg)

        elif command == 2:
            matrix_mult(winograd_alg) 

        elif command == 3:
            matrix_mult(optimized_winograd_alg)

        elif command == 4:
            compare_time()
            
            
if __name__ == "__main__": 
    main()
