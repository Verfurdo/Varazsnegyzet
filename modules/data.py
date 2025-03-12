# Kezdő mátrix (0 jelöli az üres mezőket)
kezdo_matrix = [
    [0, 0, 6, 0, 0, 4],
    [0, 2, 0, 6, 0, 0],
    [0, 4, 0, 0, 0, 5],
    [2, 0, 0, 0, 6, 0],
    [0, 0, 4, 0, 5, 0],
    [5, 0, 0, 3, 0, 0]
]

# Mintázat
mintazat = [
    [0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 0]
]

# Színek definiálása
szin_egy = "#FFECD2"
szin_ketto = "#F4B183"
keret_szin = "#000000"

# Játékszabályok szövege
szabaly_szoveg = """
A Varázsnégyzet egy logikai játék, ahol a célod, hogy kitöltsd az üres mezőket 1-től 6-ig terjedő számokkal.

Szabályok:
Töltsd ki az ábra üres mezőit 1-től 6-ig terjedő egész számokkal úgy, hogy minden
sorban és oszlopban, valamint a színnel jelölt átlókban minden szám csak egyszer szerepeljen!

Játékmenet:
1. Írd be a számokat az üres mezőkbe
2. Az "Ellenőrzés" gombbal ellenőrizheted a megoldásodat
3. Ha elakadtál, a "Megfejtés" gomb megmutatja a helyes megoldást
4. Az "Új játék" gombbal újrakezdheted a játékot

Sok sikert!
"""
