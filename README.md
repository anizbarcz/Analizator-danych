# RESEARCH DATA ANALYZER

Aplikacja konsolowa napisana w języku Python, przeznaczona do wczytywania, analizy i zapisywania danych pogodowych.

Projekt powstał w ramach szkolenia **Projektowanie i programowanie aplikacji w Pythonie...**

## Spis treści
1. [Funkcjonalności](#1-funkcjonalności)
2. [Wykorzystane technologie](#2-wykorzystane-technologie)
3. [Struktura projektu](#3-struktura-projektu)
4. [Instalacja](#4-instalacja)
5. [Uruchamianie aplikacji](#5-uruchamianie-aplikacji)
6. [Analiza danych](#6-testowanie)
7. [Testowanie](#7-testowanie)
8. [Kontrola jakości kodu](#8-kontrola-jakości-kodu)
9. [Automatyzacja CI](#9-automatyzacja-ci)
10. [Zastosowaie](#10-zastosowanie)

## 1. Funkcjonalności
![Static Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=%233776AB&labelColor=%23111111)

**Wczytaj dane z pliku csv** - Obsługa plików wejściowych w formatach CSV zawierających historyczne dane pogodowe.
**Wyświetl dane** - Wyświetlanie danych w konsoli oraz podstawowych informacji o zbiorze
**Analizuj** - Obliczanie *średniej temp maksymalnej*, *średniej temp minimalnej* oraz *sumy opadów* i wyświetlanie w konsoli 
**Generuj i zapisz wykres** - Generowanie i zapisanie wyresu na podstawie dostarczonych danych
**Zapisz dane do bazy** - Zapisywanie danych do bazy

## 2. Wykorzystane technologie
* **Python 3.12+** - główny język programowania aplikacji.
* **Pandas** - biblioteka do zaawansowanej manipulacji, parsowania i analizy danych strukturalnych.
* **Mathplotlib** - wizualizacja danych.
* **SQLite3** - wbudowany w bibliotekę standardową silnik bazy danych do trwałego zapisu danych.
* **Termcolor** - formatowanie i kolorowanie komunikatów w interfejsie konsolowym.
* **Pathlib** - obiektowe zarządzanie ścieżkami do plików i katalogów (`data/`, `database/`).
* **Pytest** - framework wykorzystywany do automatycznego testowania kodu, testy jednostkowe.
* **Ruff** - nowoczesny, szybki linter i narzędzie do automatycznego formatowania kodu.
* **Git i GitHub** - kontrola wersji i przechowywane repozytroium.
* **GitHub Action** - automatyczne uruchamianie testów i kontrola jakości kodu.
<!-- ## 3. Struktura projektu -->
## 4. Instalacja
Do uruchomienia aplikacji potrezbny jest Python w wersji 3.12+ oraz biblioteki wymienione w `requirements.txt`
1. Pobierz repozytorium projektu na swój dysk lokalny.
2. Utwórz środowisko wirtualne dla projektu:
   ```bash
   python -m venv .venv
   ```
3. Aktywuj środowisko wirtualne:
   *   **Windows (CMD/PowerShell):** `.\.venv\Scripts\Activate.ps1`
4. Zainstaluj wymagane pakiety oraz biblioteki zewnętrzne:
   ```bash
   python -m pip install -r requirements.txt
   ```
## 5. Uruchamianie
Aplikacja jest uruchamiana bezpośrednio z wiersza poleceń jako skrypt Pythona. Uruchomienie głównego pliku inicjuje pętlę menu tekstowego:
```bash
python main.py
```
Po uruchomieniu pojawia się menu z piecioma opcjami doyczącymi wczytywania, zapiswaynia i analizy danych, oraz jednej pozwalającej na wyjście z aplikacji.

Aby rzopocząć pracę należy umieścić pliki z danymi w katalogu \data
## 8. Kontrola jakości kodu

Do analizy kdu wykorzystujemy **Ruff**.

Sprawdzenie kodu - uruchomienie sprawdzenia błędów
```bash
python -m ruff check
```

Automatycznna naprawa błędów oznaczonych [*]
```bash
python -m ruff check . --fix
```

## 10. Zastosowanie
Aplikacja stanowi gotowe rozwiązanie edukacyjne oraz narzędziowe stworzone w ramach szkolenia z języka Python. Prezentuje w praktyce:
*   Zasady modułowości kodu i separacji odpowiedzialności warstw (MVC/modułowość).
*   Efektywne wykorzystanie biblioteki `pandas` do szybkiego przetwarzania danych statystycznych.
*   Pracę z relacyjnymi bazami danych w Pythonie bez użycia ciężkich zewnętrznych systemów DBMS (dzięki SQLite3).