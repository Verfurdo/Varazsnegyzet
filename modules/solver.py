import copy  # Másolat készítéséhez szükséges modul

def ures_cella_keresese(matrix):
    """Megkeresi az első üres (0 értékű) cellát a mátrixban."""
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 0:
                return (i, j)  # Az üres cella sor- és oszlopindexének visszaadása
    return None  # Ha nincs több üres cella, visszatér None értékkel

def biztonsagos_e(matrix, sor, oszlop, szam, minta):
    """Ellenőrzi, hogy a szám elhelyezhető-e a megadott cellába a szabályok szerint."""
    
    # Sor ellenőrzése – ha a szám már szerepel a sorban, nem helyezhető el
    if szam in matrix[sor]:
        return False

    # Oszlop ellenőrzése – ha a szám már szerepel az oszlopban, nem helyezhető el
    if szam in (matrix[i][oszlop] for i in range(6)):
        return False

    # Átlók ellenőrzése, ha a cella a mintában szerepel
if minta[sor][oszlop] == 1:
    # Bal felső -> jobb alsó átló ellenőrzése
    if sor == oszlop:
        for i in range(6):
            if minta[i][i] == 1 and matrix[i][i] == szam:
                return False

    # Jobb felső -> bal alsó átló ellenőrzése
    if sor + oszlop == 5:
        for i in range(6):
            j = 5 - i  # Másik átló index számítása
            if minta[i][j] == 1 and matrix[i][j] == szam:
                return False

        # Átmeneti másolat készítése a rekurzió miatt
        temp_elso_atlo = elso_atlo[:]
        if sor == oszlop and szam in temp_elso_atlo:
            if temp_elso_atlo.count(szam) > 0:
                return False

        temp_masodik_atlo = masodik_atlo[:]
        if sor + oszlop == 5 and szam in temp_masodik_atlo:
            if temp_masodik_atlo.count(szam) > 0:
                return False

    return True  # Ha a szám elhelyezhető, visszatér True értékkel

def sudoku_megoldas(matrix, minta):
    """Backtracking algoritmus a Sudoku megoldására."""
    
    ures_cella = ures_cella_keresese(matrix)
    if not ures_cella:
        return True  # Ha nincs több üres cella, a feladvány megoldódott

    sor, oszlop = ures_cella  # Az üres cella koordinátái

    for szam in range(1, 7):  # Lehetséges számok 1-től 6-ig
        if biztonsagos_e(matrix, sor, oszlop, szam, minta):
            matrix[sor][oszlop] = szam  # Szám beillesztése

            if sudoku_megoldas(matrix, minta):  
                return True  # Ha sikerült megoldani, visszatérünk

            matrix[sor][oszlop] = 0  # Backtracking: visszaállítjuk az üres állapotot

    return False  # Ha nem található megoldás, visszatér False értékkel
