# utils.py: Segédfunkciókat tartalmazó modul (üzenetablakok megjelenítése)

import tkinter as tk # Tkinter modul importálása a grafikus felhasználói felület létrehozásához

def create_message_window(master, title, message):
    """Üzenet megjelenítése külön ablakban"""
    message_window = tk.Toplevel(master) # Új, különálló ablak létrehozása a főablakhoz tartozóan
    message_window.title(title) # Ablak címének beállítása
    message_window.geometry("300x150") # Ablak méretének beállítása (300x150 pixel)
    message_window.resizable(False, False) # Ablak átméretezésének letiltása

    # Középre igazítás a főablakhoz képest
    message_window.geometry("+%d+%d" % (
        master.winfo_rootx() + master.winfo_width()//2 - 150, # X koordináta (középre igazítás)
        master.winfo_rooty() + master.winfo_height()//2 - 75  # Y koordináta (középre igazítás)
    ))

    # Üzenet szövegének megjelenítése
    msg_label = tk.Label(message_window, text=message, font=("Arial", 12), wraplength=250, pady=20)
    msg_label.pack(expand=True) # Címke elhelyezése az ablakban

    # "OK" gomb létrehozása, amely bezárja az ablakot
    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy, width=10)
    ok_button.pack(pady=10) # Gomb elhelyezése az ablakban

    # Ablak fókuszba helyezése és interakció zárolása, amíg az ablak nyitva van
    message_window.focus_set() # Fókusz az új ablakra
    message_window.grab_set() # A felhasználó csak ezt az ablakot tudja használni, amíg be nem zárja
    message_window.wait_window() # Megvárja, míg az ablak be van zárva


