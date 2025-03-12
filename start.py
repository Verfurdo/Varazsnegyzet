import os  # Operációs rendszerrel kapcsolatos műveletekhez (fájlok elérési útjának kezelése)
import sys  # Python futtatókörnyezet elérését biztosító modul importálása

# Dinamikus útvonal beállítása
aktualis_konyvtar = os.path.dirname(os.path.abspath(__file__)) # A jelenlegi szkript könyvtárának meghatározása
sys.path.append(aktualis_konyvtar) # A könyvtár a Python modulkeresési útvonalához

# Főprogram indítása
import main

if __name__ == "__main__":
    main.run()


