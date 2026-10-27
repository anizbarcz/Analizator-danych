#uruchamianie aplikacji

# from dane import pomiary
# from analiza import oblicz_srednia

# def main():
#     print("===Analizator danych===")

#     srednia = oblicz_srednia(pomiary)
#     print(f"Średnia wynosi: {srednia:.2f}")

#     #warunek uruchomienia programu - określa czy dany plik został uruchomiony bezpośrednio czy został zaimportowany jako moduł z innego pliku
#     #__name__ - zmienna automatycznie ustawiana przez Pythona dla każdego modułu
#     #"__main__" - wartość oznaczająca moduł uruchamiany jako główny program
#     if __name__ == "__main__":
#         main()
import logging

from interfejs import uruchom_menu
from logowanie import konfiguruj_logowanie


def main():
    """
    Uruchamia menu główne aplikacji
    """
    konfiguruj_logowanie()
    logging.info("Uruchomiono aplikację")

    uruchom_menu()

    logging.info("Zakończono działanie aplikacji")

if __name__ == "__main__":
    main()