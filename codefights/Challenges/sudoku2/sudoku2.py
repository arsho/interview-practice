def check_columns(grid):
    flag = True
    for i in range(9):
        ar = [0 for x in range(10)]
        for j in range(9):
            if grid[j][i]!='.':
                val = int(grid[j][i])
                if ar[val]!=0:
                    flag = False
                    return flag
                else:
                    ar[val] = 1
    return flag

def check_rows(grid):
    flag = True
    for i in range(9):
        ar = [0 for x in range(10)]
        for j in range(9):
            if grid[i][j]!='.':
                val = int(grid[i][j])
                if ar[val]!=0:
                    flag = False
                    return flag
                else:
                    ar[val] = 1
    return flag

def check_squares(grid):
    flag = True
    for i in range(0,9,3):
        for j in range(0,9,3):
            ar = [0 for x in range(10)]
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if grid[k][l]!='.':
                        val = int(grid[k][l])
                        if ar[val]!=0:
                            flag = False
                            return flag
                        else:
                            ar[val] = 1
    return flag



def sudoku2(grid):
    row_flag = check_rows(grid)
    column_flag = check_columns(grid)
    square_flag = check_squares(grid)
    if row_flag == True and column_flag == True and square_flag == True:
        return True
    else:
        return False

