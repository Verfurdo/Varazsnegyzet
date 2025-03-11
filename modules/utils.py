
import tkinter as tk

def create_message_window(master, title, message):
    """Üzenet megjelenítése külön ablakban"""
    message_window = tk.Toplevel(master)
    message_window.title(title)
    message_window.geometry("300x150")
    message_window.resizable(False, False)
    
    # Középre igazítás
    message_window.geometry("+%d+%d" % (
        master.winfo_rootx() + master.winfo_width()//2 - 150,
        master.winfo_rooty() + master.winfo_height()//2 - 75))
    
    # Üzenet szöveg
    msg_label = tk.Label(message_window, text=message, font=("Arial", 12), wraplength=250, pady=20)
    msg_label.pack(expand=True)
    
    # OK gomb
    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy, width=10)
    ok_button.pack(pady=10)
    
    # Ablak fókuszba helyezése
    message_window.focus_set()
    message_window.grab_set()
    message_window.wait_window()
