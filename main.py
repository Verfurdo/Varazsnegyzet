import os
import sys
import tkinter as tk

# Dinamikus útvonal beállítása a modulokhoz
current_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(current_dir, "modules")
sys.path.append(modules_dir)

# Modulok importálása
from modules.game import VarazsNegyzetJatek

def run():
    """Főprogram futtatása"""
    root = tk.Tk()
    root.geometry("600x400")
    jatek = VarazsNegyzetJatek(root)
    root.mainloop()

if __name__ == "__main__":
    run()
