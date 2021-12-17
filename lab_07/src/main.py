from generate import *
from dictionary import *
from alg_search import *
from read import read_command
from compare import compare_time, compare_comparsion

    
def main():
    # generate_names_surnames_file("../data/names_surnames.csv")
    # generate_db_file("../data/db.csv")

    command = -1

    dictionary = create_dictionary("../data/db.csv")

    while command != 0:
        command = read_command()
        
        if command == 1:
            search_in_dictionary(dictionary, full_search)

        elif command == 2:
           search_in_dictionary(sort_dict_by_key(dictionary), binary_search)

        elif command == 3:
            search_in_dictionary(segment_dict(sort_dict_by_key(dictionary)), segment_search)

        elif command == 4:
            compare_time()

        elif command == 5:
            compare_comparsion()


if __name__ == "__main__":
    main()
