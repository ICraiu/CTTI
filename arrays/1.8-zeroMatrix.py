# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O

# O(MxN) space complexity and O(1) time
def solution(mat):
    # iterate over each row and column
    # if one 0 is found then do a for on the row and cloud
    # after the initial iteration then iterate over the first row and first column
    # and make 0

    # i = column j = row
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
    for i in range(0, len(mat)):
        if mat[i][0] == 0:
            for j in range(0, len(mat[i])):
                mat[i][j] = 0
    for j in range(0, len(mat[0])):
        if mat[0][j] == 0:
            for i in range(0, len(mat)):
                mat[i][j] = 0
    return matrix


matrix = [[1, 1, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 1]]


assert solution(matrix) == [[1, 1, 0, 1],
                            [0, 0, 0, 0],
                            [1, 1, 0, 1]]
