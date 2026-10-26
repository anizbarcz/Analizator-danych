#interfejs konsolowy aplikacji
from termcolor import colored

from analiza import podstawowe_statystyki
from baza import zapisz_do_bazy
from dane import wczytaj_dane, wyswietl_dane
from wykresy import generuj_wykres


def wyswietl_menu():
    """
    Wyświetla menu główne w konsoli
    """


    print(colored("\n\nRESERCH DATA ANALYZER","magenta"))
    print("1. Wczytaj dane z pliku csv")
    print("2. Wyświetl dane")
    print("3. Analizuj")
    print("4. Generuj i zapisz wykres")
    print("5. Zapisz dane do bazy")
    print("0. Wyjście z programu")
    print(colored("-" * 40,"blue"))

def uruchom_menu():

    """
    Obsługuje wybór opcji w menu i wywoluje odpowiednie funkcje
    """

    dane = None

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję : ").strip()

        if wybor == "0":
            print(colored("Zakończono działanie programu","green"))
            break
        elif wybor == "1":
            print("wybrano opcję 1")
            nowe_dane = wczytaj_dane()

            if nowe_dane is not None:
                dane = nowe_dane

            # print(dane)

        elif wybor == "2":
            print("wybrano opcję 2")
            wyswietl_dane(dane)
            
        elif wybor == "3":
            print("wybrano opcję 3")
            podstawowe_statystyki(dane)
            
        elif wybor == "4":
            print("wybrano opcję 4")
            generuj_wykres(dane)
            
        elif wybor == "5":
            print("wybrano opcję 5")
            zapisz_do_bazy(dane)
            
        else:
            print(colored("Nie ma takiej opcji. Spróbuj ponownie.","red"))


