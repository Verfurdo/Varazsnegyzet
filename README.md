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
    -   `solver.py`: A játék automatikus megoldását végző algoritmus.

## Működés
A Varázsnégyzet játék célja, hogy a játékos kitöltse az üres mezőket 1-től 6-ig terjedő számokkal úgy, hogy minden sorban, oszlopban és a színnel jelölt átlókban minden szám csak egyszer szerepeljen. A program a Tkinter könyvtárat használja a grafikus felület megjelenítéséhez, és moduláris felépítése lehetővé teszi a kód könnyű karbantartását és bővítését.

## Megoldó algoritmus

A játék automatikus megoldásához rekurzív backtracking algoritmust használunk, amely a következőképpen működik:

1. Az első algoritmus üres cellát a keres a táblázatban.
2. Sorban kipróbálja az 1-től 6-ig terjedő számokat az üres cellában.
3. Minden beírt számnál ellenőrzi, hogy a lépés érvényes-e (nem sérti-e a játékszabályokat).
4. Ha a lépés érvényes, rekurzívan folytatja a következő üres cellával.
5. Ha a rekurzív hívás sikeres (megoldást talál), akkor kész a megoldás.
6. Ha nem talál érvényes számot vagy a rekurzív hívás nem talál megoldást, visszalép (backtrack), és kipróbálhatja egy másik számot az aktuális cellában.
7. Ha minden lehetőséget kipróbált és egyik sem vezetett megoldáshoz, akkor a játéknak nincs megoldása.

Ez az algoritmus garantáltan megtalálja a megoldást, ha létezik, vagy jelzi, ha nincs megoldás. 



## Közreműködők

-   [VérFürdő]

