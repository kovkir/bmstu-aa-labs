from in_out import output_table

def lev_recursion(s1, s2, output = False):
    len1 = len(s1)
    len2 = len(s2)

    if len1 == 0 or len2 == 0:
        return abs(len1 - len2)

    m = 0 if s1[-1] == s2[-1] else 1

    return min(lev_recursion(s1,      s2[:-1]) + 1,
               lev_recursion(s1[:-1], s2     ) + 1,
               lev_recursion(s1[:-1], s2[:-1]) + m)
    

def lev_table(s1, s2, output = False):
    len1 = len(s1)
    len2 = len(s2)

    M = [[i + j for j in range(len2 + 1)] 
                for i in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            m = 0 if s1[i - 1] == s2[j - 1] else 1

            M[i][j] = min(M[i - 1][j    ] + 1,
                          M[i    ][j - 1] + 1,
                          M[i - 1][j - 1] + m)
      
    if output:  
        output_table(M, s1, s2)

    return M[-1][-1]


def dam_lev_recursion(s1, s2, output = False):
    len1 = len(s1)
    len2 = len(s2)

    if len1 == 0 or len2 == 0:
        return abs(len1 - len2)

    m = 0 if s1[-1] == s2[-1] else 1

    result = min(dam_lev_recursion(s1,      s2[:-1]) + 1,
                 dam_lev_recursion(s1[:-1], s2     ) + 1,
                 dam_lev_recursion(s1[:-1], s2[:-1]) + m)

    if len1 > 1 and len2 > 1 and s1[-1] == s2[-2] \
                             and s1[-2] == s2[-1]:
        result = min(result, dam_lev_recursion(s1[:-2], s2[:-2]) + 1)

    return result
    

def dam_lev_table(s1, s2, output = False):
    len1 = len(s1)
    len2 = len(s2)

    M = [[i + j for j in range(len2 + 1)] 
                for i in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            m = 0 if s1[i - 1] == s2[j - 1] else 1

            M[i][j] = min(M[i - 1][j    ] + 1,
                          M[i    ][j - 1] + 1,
                          M[i - 1][j - 1] + m)

            if i > 1 and j > 1 and s1[i - 1] == s2[j -2 ] \
                               and s1[i - 2] == s2[j - 1]:
                M[i][j] = min(M[i][j], M[i - 2][j - 2] + 1)

    if output:  
        output_table(M, s1, s2)

    return M[-1][-1]
