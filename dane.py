#wczytywanie danych z pliku csv
from pathlib import Path

import pandas as pd
from termcolor import colored


#metoda glob służy do wyszukiwania plików, które pasują do wzorca
def wczytaj_dane():
    folder = Path("data")
    pliki = sorted(folder.glob("*.csv"))

    if not pliki:
        print(colored(f"Brak plików w folderze {folder}","red"))
        return None

    print(colored("\nDostępne pliki","blue"))
    
    for i, plik in enumerate(pliki, start =1):
        print(f"Plik nr {i}. {plik.name}")

    print("0. Powrót do menu głównego")

# pętla obsługująca wczytywanie wybreanego pliku
    while True:

        wybor = input("\nWybierz nr pliku do wczytania: ")

        if wybor == "0":
            return None

        if not wybor.isdigit():
            print(colored("Podaj poprawny numer","red"))
            continue

        numer = int(wybor)

        if numer > len(pliki):
            print(colored("Nie ma pliku o takim numerze","red"))
            continue

        wybrany_plik = pliki[numer - 1]

        try:
            df = pd.read_csv(wybrany_plik)
        except pd.errors.ParserError as blad:
            print(colored(f"Błąd wczytania pliku: {blad}","red"))
            return None
        
        print(colored(f"\nWczytano plik {wybrany_plik.name}","green"))
        print(f"Liczba wierszy: {len(df)}")

        return df


def wyswietl_dane(df):
    if df is None:
        print(colored("\nNapierw wczytaj plik csv","red"))
        return

    print("\n ********** podgląd danych **********")
    print("Pierwsze 10 wierszy")

    print(df.head(10).to_string(index = False))

    print("\nInformacje o zbiorze")
    print(f"Liczba rekordów: {df.shape[0]}")
    print(f"Liczba kolumn: {df.shape[1]}")
    print(f"Kolumny: {', '.join(df.columns)}")
    