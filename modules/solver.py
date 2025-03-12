import copy # Lehetővé teszi objektumok másolását (kezdőmátrix ne módusuljon) 

from data import mintazat 

def ures_cella_kereses(matrix):
    """Megkeresi az első üres cellát (0) a mátrixban.
    Végigmegy a mátrix sorain és oszlopain, és visszaadja az első 0-t tartalmazó cella koordinátáit.
    Ha nincs üres cella, None-t ad vissza.
    """
    for i in range(6): # Végigmegyünk a sorokon (0-tól 5-ig).
        for j in range(6): # Végigmegyünk az oszlopokon (0-tól 5-ig).
            if matrix[i][j] == 0: # Ha az aktuális cella értéke 0 (üres).
                return (i, j) # Visszaadjuk a cella koordinátáit (sor, oszlop).
    return None # Ha nincs üres cella, None-t adunk vissza.

def biztonsagos_e(matrix, sor, oszlop, szam, mintazat):
    """Ellenőrzi, hogy a szám elhelyezése a (sor, oszlop) pozícióban biztonságos-e a szabályok szerint.
    Megvizsgálja, hogy a szám szerepel-e már ugyanabban a sorban, oszlopban, illetve az átlókban (ha a cella a színes mezőkhöz tartozik).
    """
    # Sor ellenőrzése
    if szam in matrix[sor]: # Ha a 'szam' már szerepel a megadott sorban.
        return False # Nem biztonságos, mert ütközik egy már meglévő számmal.

    # Oszlop ellenőrzése
    for i in range(6): # Végigmegyünk az oszlop összes során.
        if matrix[i][oszlop] == szam: # Ha a 'szam' már szerepel a megadott oszlopban.
            return False # Nem biztonságos, mert ütközik egy már meglévő számmal.

    # Színes mezők átlóinak ellenőrzése
    if mintazat[sor][oszlop] == 1: # Ha a cella a színes mintázathoz tartozik (1-es érték jelzi).
        # Főátló ellenőrzése
        if sor == oszlop: # Ha a cella a főátlón van.
            for i in range(6): # Végigmegyünk a főátló összes celláján.
                if mintazat[i][i] == 1 and matrix[i][i] == szam and i != sor: # Ha a főátlóbeli cella is a színes mintázathoz tartozik, tartalmazza a 'szam'-ot, és nem ugyanaz a cella, amit éppen vizsgálunk.
                    return False # Nem biztonságos, mert ütközik egy már meglévő számmal a főátlón.

        # Mellékátló ellenőrzése
        if sor + oszlop == 5: # Ha a cella a mellékátlón van.
            for i in range(6): # Végigmegyünk a mellékátló összes celláján.
                if mintazat[i][5-i] == 1 and matrix[i][5-i] == szam and i != sor: # Ha a mellékátlóbeli cella is a színes mintázathoz tartozik, tartalmazza a 'szam'-ot, és nem ugyanaz a cella, amit éppen vizsgálunk.
                    return False # Nem biztonságos, mert ütközik egy már meglévő számmal a mellékátlón.
    else: # Ha a cella nem a színes mintázathoz tartozik.
        # Főátló ellenőrzése
        if sor == oszlop: # Ha a cella a főátlón van.
            for i in range(6): # Végigmegyünk a főátló összes celláján.
                if matrix[i][i] == szam and i != sor: # Ha a főátlóbeli cella tartalmazza a 'szam'-ot, és nem ugyanaz a cella, amit éppen vizsgálunk.
                    return False # Nem biztonságos, mert ütközik egy már meglévő számmal a főátlón.

        # Mellékátló ellenőrzése
        if sor + oszlop == 5: # Ha a cella a mellékátlón van.
            for i in range(6): # Végigmegyünk a mellékátló összes celláján.
                if matrix[i][5-i] == szam and i != sor: # Ha a mellékátlóbeli cella tartalmazza a 'szam'-ot, és nem ugyanaz a cella, amit éppen vizsgálunk.
                    return False # Nem biztonságos, mert ütközik egy már meglévő számmal a mellékátlón.

    return True # Ha a szám elhelyezése biztonságos, True-t adunk vissza.

def varazs_negyzet_megoldasa(matrix, mintazat):
    """Backtracking algoritmus a Sudoku megoldására.
    Rekurzív függvény, ami végigmegy az üres cellákon, és megpróbálja beilleszteni a számokat 1-től 6-ig.
    Ha egy szám beillesztése biztonságos, rekurzívan meghívja önmagát a következő üres cellára.
    Ha a rekurzív hívás True-t ad vissza, akkor a megoldás megtalálható, és True-t adunk vissza.
    Ha a rekurzív hívás False-t ad vissza, akkor a számot eltávolítjuk a cellából, és megpróbálunk egy másik számot beilleszteni.
    Ha nincs több üres cella, akkor a megoldás megtalálható, és True-t adunk vissza.
    Ha nincs megoldás, False-t adunk vissza.
    """
    ures_cella = ures_cella_kereses(matrix) # Megkeressük az első üres cellát.
    if not ures_cella: # Ha nincs üres cella (a mátrix teljesen ki van töltve).
        return True # A megoldás megtalálható.

    sor, oszlop = ures_cella # Lekérjük az üres cella koordinátáit.

    for szam in range(1, 7): # Végigmegyünk a számokon 1-től 6-ig.
        if biztonsagos_e(matrix, sor, oszlop, szam, mintazat): # Ha a szám elhelyezése biztonságos az adott cellában.
            matrix[sor][oszlop] = szam # Beírjuk a számot a cellába.
            if varazs_negyzet_megoldasa(matrix, mintazat): # Rekurzívan meghívjuk a függvényt a következő üres cellára.
                return True # Ha a rekurzív hívás True-t ad vissza, a megoldás megtalálható.
            matrix[sor][oszlop] = 0  # Ha a rekurzív hívás False-t ad vissza, visszaállítjuk a cellát 0-ra (backtracking).

    return False # Ha egyik szám sem helyezhető el biztonságosan az adott cellában, False-t adunk vissza (nincs megoldás).

def megold(kezdo_matrix):
    """Megoldja a varázsnégyzetet a megadott kezdőmátrix alapján.
    Létrehoz egy másolatot a kezdőmátrixról, és meghívja a varazs_negyzet_megoldasa függvényt.
    Ha a megoldás megtalálható, visszaadja a megoldott mátrixot, egyébként None-t.
    """
    matrix = copy.deepcopy(kezdo_matrix) # Létrehozunk egy másolatot a kezdőmátrixról, hogy ne módosítsuk az eredetit.
    if varazs_negyzet_megoldasa(matrix, mintazat): # Meghívjuk a varázsnégyzet megoldó függvényt a másolaton.
        return matrix # Ha a megoldás megtalálható, visszaadjuk a megoldott mátrixot.
    else:
        return None # Ha nincs megoldás, None-t adunk vissza.
