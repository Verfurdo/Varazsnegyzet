import tkinter as tk # Tkinter GUI könyvtár importálása
from modules.data import szin_egy, szin_ketto, keret_szin, mintazat, szabaly_szoveg # Szükséges adatok importálása

class GameUI:
    """Játék felhasználói felületét kezelő osztály"""
    def __init__(self, master):
        """Az osztály inicializálása, a GUI elemek létrehozása"""
        self.master = master

        # Főkeret létrehozása
        self.fo_keret = tk.Frame(master)
        self.fo_keret.pack(fill=tk.BOTH, expand=True)

        # Bal oldali keret a játéktáblának
        self.bal_keret = tk.Frame(self.fo_keret)
        self.bal_keret.pack(side=tk.LEFT, padx=10, pady=10)

        # Jobb oldali keret a játékszabályoknak
        self.jobb_keret = tk.Frame(self.fo_keret)
        self.jobb_keret.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Vászon méretei
        self.cella_meret = 50
        self.vaszon_szelesseg = 300
        self.vaszon_magassag = 300

        # Vászon létrehozása a bal oldali keretben
        self.vaszon = tk.Canvas(self.bal_keret, width=self.vaszon_szelesseg,
                                height=self.vaszon_magassag, highlightthickness=0)
        self.vaszon.pack()

        # Gombok kerete a bal oldalon
        self.gomb_keret = tk.Frame(self.bal_keret)
        self.gomb_keret.pack(pady=10)

        # Játékszabályok megjelenítése a jobb oldali keretben
        self.szabalyok_megjelenitese()

    def gombok_letrehozasa(self, ellenorzes_parancs, megfejtes_parancs, ujra_parancs, kilepes_parancs):
        """Gombok létrehozása"""
        self.ellenorzes_gomb = tk.Button(self.gomb_keret, text="Ellenőrzés", command=ellenorzes_parancs)
        self.ellenorzes_gomb.pack(side=tk.LEFT, padx=5)
        self.megfejtes_gomb = tk.Button(self.gomb_keret, text="Megfejtés", command=megfejtes_parancs)
        self.megfejtes_gomb.pack(side=tk.LEFT, padx=5)
        self.ujra_gomb = tk.Button(self.gomb_keret, text="Új játék", command=ujra_parancs)
        self.ujra_gomb.pack(side=tk.LEFT, padx=5)
        self.kilepes_gomb = tk.Button(self.gomb_keret, text="Kilépés", command=kilepes_parancs)
        self.kilepes_gomb.pack(side=tk.LEFT, padx=5)

    def szabalyok_megjelenitese(self):
        """Játékszabályok megjelenítése"""
        # Cím létrehozása
        szabaly_cim = tk.Label(self.jobb_keret, text="Játékszabályok", font=("Arial", 14, "bold"))
        szabaly_cim.pack(pady=(0, 10))

        # Játékszabályok szövegének megjelenítése
        szabaly_szoveg_cimke = tk.Label(self.jobb_keret, text=szabaly_szoveg, justify=tk.LEFT, wraplength=250)
        szabaly_szoveg_cimke.pack(fill=tk.BOTH, expand=True)

    def cella_kirajzolasa(self, i, j, value=None, entry=None):
        """Egy cella kirajzolása a játéktáblán"""
        x1, y1 = j * self.cella_meret, i * self.cella_meret
        x2, y2 = x1 + self.cella_meret, y1 + self.cella_meret

        # Cellaszín meghatározása a mintázat alapján
        kitolto_szin = szin_egy if mintazat[i][j] == 1 else szin_ketto

        # Négyzet rajzolása
        self.vaszon.create_rectangle(x1, y1, x2, y2, fill=kitolto_szin, outline=keret_szin, width=2)

        # Ha van érték, azt szövegként kiírjuk a cellába
        if value:
            self.vaszon.create_text(x1 + self.cella_meret / 2,
                                    y1 + self.cella_meret / 2,
                                    text=str(value),
                                    font=("Arial", 16))
        return (x1, y1)  # A cella bal felső koordinátáját visszaadjuk

    def tabla_keret_kirajzolasa(self):
        """A játéktábla keretének kirajzolása"""
        self.vaszon.create_rectangle(0, 0, self.vaszon_szelesseg, self.vaszon_magassag,
                                outline=keret_szin, width=4)
