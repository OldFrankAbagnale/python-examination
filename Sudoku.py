import numpy as np  # Numpy for easy work with matrice



def check_no_dups(niners):         #проверяем дубликаты в*
    uniqueDigits = set()
    for num in niners:
        if num != 0:
            if num in uniqueDigits:
                return False
        uniqueDigits.add(num)
    return True


def check_row(grid, row):  #чекаем строки
    nineGrouping = []
    for cell in grid[row]:
        nineGrouping.append(cell)
    return check_no_dups(nineGrouping)


def check_column(grid, column):#чекаем столбцы
    nineGrouping = []
    for row in grid:
        nineGrouping.append(row[column])
    return check_no_dups(nineGrouping)





def check_subgrid(grid, row, column): #проверяем квадраты
    nineGrouping = []
    for i in range(row, row + 3):
        for j in range(column, column + 3):
            nineGrouping.append(grid[i][j])
    return check_no_dups(nineGrouping)


def check_sudoku(file_name):         #основная функция
    grid = np.loadtxt(file_name + '.txt', usecols=range(9))

    for i in range(0, 9):
        if not check_row(grid, i):
            return False
        if not check_column(grid, i):
            return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not check_subgrid(grid, i, j):
                return False

    return True
    pass

