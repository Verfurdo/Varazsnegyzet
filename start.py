import os
import sys

# Dinamikus útvonal beállítása
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Főprogram indítása
import main

if __name__ == "__main__":
    main.run()
