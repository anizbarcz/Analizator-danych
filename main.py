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
from interfejs import uruchom_menu


def main():
    uruchom_menu()

if __name__ == "__main__":
    main()