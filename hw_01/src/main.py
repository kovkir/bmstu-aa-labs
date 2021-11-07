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

    print("\n\nРасстояние Левенштейна равно: %d\n" %(table[-1][-1]))

def levenstein_table():

    s1 = input("\nВведите 1-ую строку: ")           # 1
    s2 = input("Введите 2-ую строку: ")             # 2

    len1 = len(s1)                                  # 3
    len2 = len(s2)                                  # 4

    M = [[0] * (len2 + 1) for _ in range(len1 + 1)] # 5

    for i in range(len1 + 1):                       # 6    
        M[i][0] = i                                 # 7
    
    for j in range(len2 + 1):                       # 8   
        M[0][j] = j                                 # 9   

    for i in range(1, len1 + 1):                    # 10   
        for j in range(1, len2 + 1):                # 11
                              
            A = M[i - 1][j    ] + 1                 # 12
            D = M[i    ][j - 1] + 1                 # 13
            C = M[i - 1][j - 1]                     # 14
            
            if s1[i - 1] != s2[j - 1]:              # 15
                C += 1                              # 16

            M[i][j] = min(A, D, C)                  # 17

    output_table(M, s1, s2)

    return M[-1][-1]

if __name__ == "__main__": 
    levenstein_table()
