
import tkinter as tk
from modules.data import initial_matrix, solution_matrix
from modules.ui import GameUI
from modules.utils import create_message_window

class VarazsNegyzetJatek:
    """Varázsnégyzet játék fő osztálya"""
    
    def __init__(self, master):
        self.master = master
        master.title("Varázsnégyzet Játék")
        
        # UI inicializálása
        self.ui = GameUI(master)
        
        # Játék adatok inicializálása
        self.matrix = [row[:] for row in initial_matrix]
        self.entries = {}
        
        # Játéktábla kirajzolása
        self.draw_grid()
        
        # Gombok létrehozása
        self.ui.create_buttons(
            check_command=self.check_solution,
            solution_command=self.show_solution,
            reset_command=self.reset_game,
            exit_command=self.exit_game
        )
    
    def draw_grid(self):
        """Játéktábla kirajzolása"""
        self.entries = {}
        
        for i in range(6):
            for j in range(6):
                # Cella kirajzolása
                x1, y1 = self.ui.draw_cell(i, j, 
                                         value=initial_matrix[i][j] if initial_matrix[i][j] != 0 else None)
                
                # Ha a kezdeti mátrixban 0 van, akkor beviteli mezőt hozunk létre
                if initial_matrix[i][j] == 0:
                    vcmd = (self.master.register(self.validate_entry), '%P')
                    entry = tk.Entry(self.ui.left_frame, width=2, font=("Arial", 16), 
                                    justify='center', validate='key', validatecommand=vcmd)
                    entry.place(x=x1 + self.ui.cell_size / 2 - 10, y=y1 + self.ui.cell_size / 2 - 12)
                    self.entries[(i, j)] = entry
        
        # Tábla keretének kirajzolása
        self.ui.draw_border()
    
    def validate_entry(self, value):
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
    
    def check_solution(self):
        """Megoldás ellenőrzése"""
        # Beolvassuk a beviteli mezők tartalmát
        current_matrix = [row[:] for row in initial_matrix]
        
        for (i, j), entry in self.entries.items():
            value = entry.get()
            if value:  # Csak a kitöltött mezőket dolgozzuk fel
                try:
                    num = int(value)
                    current_matrix[i][j] = num
                except ValueError:
                    create_message_window(self.master, "Hiba", 
                                        f"A(z) {i+1}. sor {j+1}. oszlopában lévő érték nem szám!")
                    return
        
        # Ellenőrizzük, hogy minden mező ki van-e töltve
        if any(0 in row for row in current_matrix):
            create_message_window(self.master, "Figyelem", "Még nem töltöttél ki minden mezőt!")
            return
        
        # Összehasonlítjuk a beírt értékeket a megoldással
        if current_matrix == solution_matrix:
            create_message_window(self.master, "Gratulálunk!", "A megoldásod helyes!\nNyertél!")
        else:
            create_message_window(self.master, "Sajnos nem nyertél", "A megoldás nem helyes.\nPróbáld újra!")
    
    def show_solution(self):
        """Megoldás megjelenítése"""
        # Először töröljük a beviteli mezőket
        for (i, j), entry in self.entries.items():
            entry.destroy()
        
        self.ui.canvas.delete("all")  # Töröljük a canvas tartalmát
        
        # Kirajzoljuk a megoldást
        for i in range(6):
            for j in range(6):
                self.ui.draw_cell(i, j, value=solution_matrix[i][j])
        
        # Tábla keretének kirajzolása
        self.ui.draw_border()
    
    def reset_game(self):
        """Játék újraindítása"""
        # Töröljük a beviteli mezőket
        for (i, j), entry in self.entries.items():
            entry.destroy()
        
        self.ui.canvas.delete("all")  # Töröljük a canvas tartalmát
        self.matrix = [row[:] for row in initial_matrix]  # Visszaállítjuk a kezdeti állapotot
        self.draw_grid()  # Újrarajzoljuk a táblát

    def exit_game(self):
        """Kilépés a játékból"""
        self.master.destroy()
