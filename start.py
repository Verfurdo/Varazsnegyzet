# start.py: A program belépési pontja, útvonalakat tölt be és elindítja a programot.

import os # Operációs rendszerrel kapcsolatos műveletekhez (fájlok elérési útjának kezelése)
import sys # Python futtatókörnyezet elérését biztosító modul importálása

# Dinamikus útvonal beállítása
current_dir = os.path.dirname(os.path.abspath(__file__)) # A jelenlegi szkript könyvtárának meghatározása
sys.path.append(current_dir) # A könyvtár a Python modulkeresési útvonalához

# Főprogram indítása
import main

if __name__ == "__main__":
    main.run()
