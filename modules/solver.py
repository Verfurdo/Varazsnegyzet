import copy 

from data import mintazat 

def ures_cella_kereses(matrix):
    """Megkeresi az első üres cellát (0) a mátrixban."""
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 0:
                return (i, j)
    return None

def biztonsagos_e(matrix, sor, oszlop, szam, mintazat):
    """Ellenőrzi, hogy a szám elhelyezése a (sor, oszlop) pozícióban biztonságos-e a szabályok szerint."""
    # Sor ellenőrzése
    if szam in matrix[sor]:
        return False

    # Oszlop ellenőrzése
    for i in range(6):
        if matrix[i][oszlop] == szam:
            return False

    # Színes mezők átlóinak ellenőrzése
    if mintazat[sor][oszlop] == 1:
        # Főátló ellenőrzése
        if sor == oszlop:
            for i in range(6):
                if mintazat[i][i] == 1 and matrix[i][i] == szam and i != sor:
                    return False

        # Mellékátló ellenőrzése
        if sor + oszlop == 5:
            for i in range(6):
                if mintazat[i][5-i] == 1 and matrix[i][5-i] == szam and i != sor:
                    return False
    else:
        # Főátló ellenőrzése
        if sor == oszlop:
            for i in range(6):
                if matrix[i][i] == szam and i != sor:
                    return False

        # Mellékátló ellenőrzése
        if sor + oszlop == 5:
            for i in range(6):
                if matrix[i][5-i] == szam and i != sor:
                    return False

    return True

def varazs_negyzet_megoldasa(matrix, mintazat):
    """Backtracking algoritmus a Sudoku megoldására."""
    ures_cella = ures_cella_kereses(matrix)
    if not ures_cella:
        return True

    sor, oszlop = ures_cella

    for szam in range(1, 7):
        if biztonsagos_e(matrix, sor, oszlop, szam, mintazat):
            matrix[sor][oszlop] = szam
            if varazs_negyzet_megoldasa(matrix, mintazat):
                return True
            matrix[sor][oszlop] = 0  

    return False

def megold(kezdo_matrix):
    matrix = copy.deepcopy(kezdo_matrix)
    if varazs_negyzet_megoldasa(matrix, mintazat):
        return matrix
    else:
        return None
