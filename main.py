# main.py: Inicializálja a játék felületét és meghívja a modulokat.

import os  # Operációs rendszerrel kapcsolatos műveletekhez (fájlok elérési útjának kezelése)
import sys  # A Python futtatókörnyezet elérését biztosító modul
import tkinter as tk  # Grafikus felhasználói felület (GUI) létrehozására szolgáló modul

# Dinamikus útvonal beállítása a modulokhoz
current_dir = os.path.dirname(os.path.abspath(__file__))  # A jelenlegi szkript könyvtárának elérési útja
modules_dir = os.path.join(current_dir, "modules")  # A "modules" alkönyvtár teljes elérési útja
sys.path.append(modules_dir)  # A "modules" könyvtár hozzáadása a Python modulkeresési útvonalához

# Modulok importálása
from modules.game import VarazsNegyzetJatek  # A VarazsNegyzetJatek osztály importálása a modules/game.py fájlból

def run():
    """Főprogram futtatása"""
    root = tk.Tk()  # A Tkinter főablak (root) létrehozása
    root.geometry("600x400")  # Az ablak méretének beállítása (600x400 pixel)
    jatek = VarazsNegyzetJatek(root)  # A játék inicializálása a Tkinter ablakban
    root.mainloop()  # Az alkalmazás fő ciklusának elindítása (ablak megjelenítése és kezelése)

if __name__ == "__main__":
    run()  # Ha a fájlt közvetlenül futtatják, akkor elindítja a GUI alkalmazást
