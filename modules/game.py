import tkinter as tk # 
from modules.data import kezdo_matrix, mintazat # 
from modules.ui import GameUI # 
from modules.utils import create_message_window # 
from modules import solver # 
import copy # 

class VarazsNegyzetJatek:
    """Varázsnégyzet játék fő osztálya"""
    def __init__(self, master):
        self.master = master
        master.title("Varázsnégyzet Játék")

        # UI inicializálása
        self.ui = GameUI(master)

        # Játék adatok inicializálása
        self.kezdo_matrix = [row[:] for row in kezdo_matrix] 
        self.matrix = [row[:] for row in kezdo_matrix]
        self.beviteli_mezok = {}

        # Játéktábla kirajzolása
        self.tabla_kirajzolasa()

        # Gombok létrehozása
        self.ui.gombok_letrehozasa(
            ellenorzes_parancs=self.megoldas_ellenorzese,
            megfejtes_parancs=self.megoldas_megjelenitese, 
            ujra_parancs=self.jatek_ujrainditasa,
            kilepes_parancs=self.kilepes_a_jatekbol
        )

    def tabla_kirajzolasa(self):
        """Játéktábla kirajzolása"""
        self.beviteli_mezok = {}
        for i in range(6):
            for j in range(6):
                # Cella kirajzolása
                x1, y1 = self.ui.cella_kirajzolasa(i, j,
                                               value=self.kezdo_matrix[i][j] if self.kezdo_matrix[i][j] != 0 else None)

                # Ha a kezdeti mátrixban 0 van, akkor beviteli mezőt hozunk létre
                if self.kezdo_matrix[i][j] == 0:
                    vcmd = (self.master.register(self.beviteli_mezo_validalasa), '%P')
                    entry = tk.Entry(self.ui.bal_keret, width=2, font=("Arial", 16),
                                       justify='center', validate='key', validatecommand=vcmd)
                    entry.place(x=x1 + self.ui.cella_meret / 2 - 10, y=y1 + self.ui.cella_meret / 2 - 12)
                    self.beviteli_mezok[(i, j)] = entry

        # Tábla keretének kirajzolása
        self.ui.tabla_keret_kirajzolasa()

    def beviteli_mezo_validalasa(self, value):
        """Beviteli mező validálása"""
        if value == "":
            return True
        try:
            num = int(value)
            if 1 <= num <= 6:  # Csak 1 és 6 közötti számok engedélyezettek
                return True
            else:
                create_message_window(self.master, "Hiba", "Csak 1 és 6 közötti számokat adhatsz meg!")
                return False
        except ValueError:
            create_message_window(self.master, "Hiba", "Csak számokat adhatsz meg!")
            return False

    def megoldas_ellenorzese(self):
        """Megoldás ellenőrzése"""
        # Beolvassuk a beviteli mezők tartalmát
        aktualis_matrix = [row[:] for row in self.kezdo_matrix]
        for (i, j), entry in self.beviteli_mezok.items():
            value = entry.get()
            if value:  # Csak a kitöltött mezőket dolgozzuk fel
                try:
                    num = int(value)
                    aktualis_matrix[i][j] = num
                except ValueError:
                    create_message_window(self.master, "Hiba",
                                          f"A(z) {i + 1}. sor {j + 1}. oszlopában lévő érték nem szám!")
                    return

        # Ellenőrizzük, hogy minden mező ki van-e töltve
        if any(0 in row for row in aktualis_matrix):
            create_message_window(self.master, "Figyelem", "Még nem töltöttél ki minden mezőt!")
            return

        if self.helyes_e_a_megoldas(aktualis_matrix):
            create_message_window(self.master, "Gratulálunk!", "A megoldásod helyes!\nNyertél!")
        else:
            create_message_window(self.master, "Sajnos nem nyertél", "A megoldás nem helyes.\nPróbáld újra!")

    def helyes_e_a_megoldas(self, matrix):
        """Ellenőrzi, hogy a megadott mátrix helyes megoldás-e."""
        # Sorok és oszlopok ellenőrzése
        for i in range(6):
            if len(set(matrix[i])) != 6 or any(matrix[i].count(n) > 1 for n in range(1, 7)):
                return False
            if len(set(matrix[j][i] for j in range(6))) != 6 or any(
                    list(matrix[j][i] for j in range(6)).count(n) > 1 for n in range(1, 7)):
                return False

        # Színes átlók ellenőrzése
        atlo1 = []
        atlo2 = []
        for i in range(6):
            for j in range(6):
                if mintazat[i][j] == 1:
                    if i == j:
                        atlo1.append(matrix[i][j])
                    if i + j == 5:
                        atlo2.append(matrix[i][j])

        if len(set(atlo1)) != len(atlo1) or len(set(atlo2)) != len(atlo2) or len(atlo1) != len(set(atlo1)) or len(
                atlo2) != len(set(atlo2)):
            return False

        return True

    def megoldas_megjelenitese(self):
        """Megoldja a rejtvényt, és megjeleníti a megoldást."""
        matrix_copy = copy.deepcopy(self.kezdo_matrix)
        solved_matrix = solver.megold(matrix_copy) 
        if solved_matrix:
            # Display the solved matrix
            self.megoldas_kirajzolasa(solved_matrix)
        else:
            create_message_window(self.master, "Sajnálom", "Nem található megoldás.")

    def megoldas_kirajzolasa(self, solved_matrix):
        """Megjeleníti a megoldott mátrixot a táblán."""
        # Clear existing entries
        for (i, j), entry in self.beviteli_mezok.items():
            entry.destroy()

        self.ui.vaszon.delete("all")

        # Draw the solved matrix on the canvas
        for i in range(6):
            for j in range(6):
                self.ui.cella_kirajzolasa(i, j, value=solved_matrix[i][j])

        self.ui.tabla_keret_kirajzolasa()  # Redraw the border

    def jatek_ujrainditasa(self):
        """Játék újraindítása"""
        # Töröljük a beviteli mezőket
        for (i, j), entry in self.beviteli_mezok.items():
            entry.destroy()

        self.ui.vaszon.delete("all")  # Töröljük a canvas tartalmát
        self.matrix = [row[:] for row in self.kezdo_matrix]  # Visszaállítjuk a kezdeti állapotot
        self.tabla_kirajzolasa()  # Újrarajzoljuk a táblát

    def kilepes_a_jatekbol(self):
        """Kilépés a játékból"""
        self.master.destroy()
