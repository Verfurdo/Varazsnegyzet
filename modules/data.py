
# Kezdő mátrix (0 jelöli az üres mezőket)
initial_matrix = [
    [0, 0, 6, 0, 0, 4],
    [0, 2, 0, 6, 0, 0],
    [0, 4, 0, 0, 0, 5],
    [2, 0, 0, 0, 6, 0],
    [0, 0, 4, 0, 5, 0],
    [5, 0, 0, 3, 0, 0]
]

# Megoldás mátrix
solution_matrix = [
    [1, 3, 6, 5, 2, 4],
    [4, 2, 5, 6, 3, 1],
    [6, 4, 3, 2, 1, 5],
    [2, 5, 1, 4, 6, 3],
    [3, 6, 4, 1, 5, 2],
    [5, 1, 2, 3, 4, 6]
]

# Mintázat
pattern = [
    [0, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 0]
]

# Színek definiálása
color1 = "#FFECD2"
color2 = "#F4B183"
border_color = "#000000"

# Játékszabályok szövege
rules_text = """
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
