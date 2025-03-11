# modules/solver.py
import copy

def find_empty_cell(matrix):
    """Finds the first empty cell (0) in the matrix."""
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 0:
                return (i, j)
    return None

def is_safe(matrix, row, col, num, pattern):
    """Checks if placing num at (row, col) is safe according to the rules."""
    # Row check
    if num in matrix[row]:
        return False

    # Column check
    if num in (matrix[i][col] for i in range(6)):
        return False

     # Átlók ellenőrzése (csak a releváns átlókat)
    if pattern[row][col] == 1:
        # Ellenőrizzük, hogy a szám szerepel-e a megfelelő átlóban
        diag1 = []
        diag2 = []

        for i in range(6):
            for j in range(6):
                if pattern[i][j] == 1:
                    if i == j:
                        diag1.append(matrix[i][j])
                    if i + j == 5:
                        diag2.append(matrix[i][j])

        #Azért kell kivenni a num-ot, hogy a rekurzió működjön
        temp_diag1 = diag1[:]
        if row == col:
            if num in temp_diag1:
                if temp_diag1.count(num) > 0:
                     return False

        temp_diag2 = diag2[:]

        if row + col == 5:
            if num in temp_diag2:
                if temp_diag2.count(num) > 0:
                    return False

    return True

def solve_sudoku(matrix, pattern):
    """Solves the Sudoku puzzle using backtracking."""
    empty_cell = find_empty_cell(matrix)
    if not empty_cell:
        return True  # No more empty cells, puzzle solved

    row, col = empty_cell

    for num in range(1, 7):
        if is_safe(matrix, row, col, num, pattern):
            matrix[row][col] = num

            if solve_sudoku(matrix, pattern):
                return True  # Solution found

            matrix[row][col] = 0  # Backtrack

    return False  # No solution found
