m = [["x" for x in range(16)] for y in range(16)]

m[0][15] = [1, 2, 3]
m[1][15] = [2, 4, 3]
m[2][15] = [2, 8]
m[3][15] = [3, 1, 6]
m[4][15] = [5, 5]
m[5][15] = [4, 4]
m[6][15] = [3, 4]
m[7][15] = [1, 4, 5]
m[8][15] = [1, 8, 1]
m[9][15] = [2, 6, 1]
m[10][15] = [3, 4, 3]
m[11][15] = [4, 2, 4]
m[12][15] = [4, 2, 4]
m[13][15] = [5, 2, 4]
m[14][15] = [11]

m[15][0] = [5]
m[15][1] = [5]
m[15][2] = [5, 5]
m[15][3] = [8, 4]
m[15][4] = [6, 3]
m[15][5] = [6, 2]
m[15][6] = [4, 4, 1]
m[15][7] = [3, 7]
m[15][8] = [4, 8]
m[15][9] = [10, 1]
m[15][10] = [8, 3]
m[15][11] = [8, 4]
m[15][12] = [8, 5]
m[15][13] = [5, 4]
m[15][14] = [1, 4]


def print_matrix():
    for x in m:
        print(*x)


print_matrix()
