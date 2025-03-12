# ui.py: A grafikus felületet kezelő modul a `GameUI` osztály segítségével

import tkinter as tk  # Tkinter GUI könyvtár importálása
from modules.data import color1, color2, border_color, pattern, rules_text  # Szükséges adatok importálása

class GameUI:
    """Játék felhasználói felületét kezelő osztály"""
    
    def __init__(self, master):
        """Az osztály inicializálása, a GUI elemek létrehozása"""
        self.master = master
        
        # Főkeret létrehozása
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Bal oldali keret a játéktáblának
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Jobb oldali keret a játékszabályoknak
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Vászon méretei
        self.cell_size = 50
        self.canvas_width = 300
        self.canvas_height = 300
        
        # Vászon létrehozása a bal oldali keretben
        self.canvas = tk.Canvas(self.left_frame, width=self.canvas_width, 
                               height=self.canvas_height, highlightthickness=0)
        self.canvas.pack()
        
        # Gombok kerete a bal oldalon
        self.button_frame = tk.Frame(self.left_frame)
        self.button_frame.pack(pady=10)
        
        # Játékszabályok megjelenítése a jobb oldali keretben
        self.show_rules()
    
    def create_buttons(self, check_command, solution_command, reset_command, exit_command):
        """Gombok létrehozása"""
        self.ellenorzes_button = tk.Button(self.button_frame, text="Ellenőrzés", command=check_command)
        self.ellenorzes_button.pack(side=tk.LEFT, padx=5)
    
        self.megfejtes_button = tk.Button(self.button_frame, text="Megfejtés", command=solution_command)
        self.megfejtes_button.pack(side=tk.LEFT, padx=5)
    
        self.ujra_button = tk.Button(self.button_frame, text="Új játék", command=reset_command)
        self.ujra_button.pack(side=tk.LEFT, padx=5)
    
        self.kilepes_button = tk.Button(self.button_frame, text="Kilépés", command=exit_command)
        self.kilepes_button.pack(side=tk.LEFT, padx=5)
    
    def show_rules(self):
        """Játékszabályok megjelenítése"""
        # Cím létrehozása
        rules_title = tk.Label(self.right_frame, text="Játékszabályok", font=("Arial", 14, "bold"))
        rules_title.pack(pady=(0, 10))
        
        # Játékszabályok szövegének megjelenítése
        rules_label = tk.Label(self.right_frame, text=rules_text, justify=tk.LEFT, wraplength=250)
        rules_label.pack(fill=tk.BOTH, expand=True)
    
    def draw_cell(self, i, j, value=None, entry=None):
        """Egy cella kirajzolása a játéktáblán"""
        x1, y1 = j * self.cell_size, i * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        
        # Cellaszín meghatározása a mintázat alapján
        fill_color = color1 if pattern[i][j] == 1 else color2
        
        # Négyzet rajzolása
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline=border_color, width=2)
        
        # Ha van érték, azt szövegként kiírjuk a cellába
        if value:
            self.canvas.create_text(x1 + self.cell_size / 2,
                                   y1 + self.cell_size / 2,
                                   text=str(value),
                                   font=("Arial", 16))
        
        return (x1, y1)  # A cella bal felső koordinátáját visszaadjuk
    
    def draw_border(self):
        """A játéktábla keretének kirajzolása"""
        self.canvas.create_rectangle(0, 0, self.canvas_width, self.canvas_height, 
                                    outline=border_color, width=4)
