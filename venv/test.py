def minesweeper(matrix):
    out = []
    for i in range(len(matrix)):
        out.append([0] * len(matrix[0]))
    lst = [(-1, -1), (-1, +0), (-1, +1), (+0, -1), (+0, +1), (+1, -1), (+1, +0), (+1, +1)]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            count = 0
            for x, y in lst:
                try:
                    i_val = row + x
                    j_val = column + y
                    if i_val >-1 and j_val > -1:
                        if matrix[i_val][j_val]:
                            count += 1
                except IndexError as error:
                    continue
            out[row][column] = count
            print(count)
            break
        break
    return out

matrix =[[True, False, False, True],[False, False, True, False],[True, True, False, True]]
minesweeper(matrix)


