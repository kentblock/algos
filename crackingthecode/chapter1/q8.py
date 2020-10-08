# Cracking the code question 1.8 Zero matrix

def zero_matrix(matrix):
    """
    returns matrix where each row and column are zeroed if they contain 
    the value 0
    """
    # simple solution - two passes over matrix, first one collected rows/cols to 0
    #   second one zero the rows and cols
    cols = []
    rows = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                cols.append(i)
                rows.append(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in cols or j in rows:
                matrix[i][j] = 0

if __name__ == "__main__":
    
    m1 = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
    zero_matrix(m1)
    print(m1)

    m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    zero_matrix(m2)
    print(m2)

    m3 = [[0, 1, 1], [1, 1, 0], [1, 1, 1]]
    zero_matrix(m3)
    print(m3)