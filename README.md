# Varázsnégyzet Játék

Egy logikai játék Pythonban, Tkinter könyvtár segítségével. A játék célja, hogy a felhasználó kitöltse a 6x6-os táblázat üres mezőit 1-től 6-ig terjedő számokkal úgy, hogy minden sorban, oszlopban és a színnel jelölt átlókban minden szám csak egyszer szerepeljen.

## Tartalom

- [Előfeltételek](#elofeltetelek)
- [Telepítés](#telepites)
- [Használat](#hasznalat)
- [Fájlok magyarázata](#fajlok-magyarazata)
- [Működés](#mukodes)
- [Közreműködők](#kozremukodok)

## Előfeltételek

A projekt az alábbi Python könyvtárakat használja:

- Tkinter (általában a Python alap telepítés része)

## Telepítés

1.  Klónozd a repository-t:

    ```
    git clone https://github.com/Verfurdo/Varazsnegyzet.git
    ```

2.  Navigálj a projekt könyvtárába:

    ```
    cd [repository_neve]
    ```

3.  Futtasd a `start.py` fájlt a játék elindításához:

    ```
    python start.py
    ```

## Használat

A játék elindítása után a következő lehetőségek állnak rendelkezésre:

-   **Számok beírása:** Kattints az üres mezőkre és írd be a megfelelő számot (1-6).
-   **Megoldás ellenőrzése:** Ellenőrizd, hogy a táblázat helyesen van-e kitöltve.
-   **Megoldás megtekintése:** A helyes megoldás megtekintése.
-   **Új játék:** Új játék indítása véletlenszerűen generált kezdőtáblával.
-   **Kilépés:** Játékból való kilépés.

## Fájlok magyarázata

-   `start.py`: A program belépési pontja, útvonalakat tölt be és elindítja a programot.
-   `main.py`: Inicializálja a játék felületét és meghívja a modulokat.
-   `modules/`:
    -   `game.py`: A játék fő logikáját tartalmazza a `VarazsNegyzetJatek` osztállyal.
    -   `ui.py`: A felhasználói felületet kezeli a `GameUI` osztály segítségével.
    -   `data.py`: A játék adatait tárolja (kezdő mátrix, megoldás mátrix, színek, szabályok).
    -   `utils.py`: Segédfunkciókat tartalmaz (pl. üzenetablakok megjelenítése).

## Működés
A Varázsnégyzet játék célja, hogy a játékos kitöltse az üres mezőket 1-től 6-ig terjedő számokkal úgy, hogy minden sorban, oszlopban és a színnel jelölt átlókban minden szám csak egyszer szerepeljen. A program a Tkinter könyvtárat használja a grafikus felület megjelenítéséhez, és moduláris felépítése lehetővé teszi a kód könnyű karbantartását és bővítését.

## Közreműködők

-   [VérFürdő]

