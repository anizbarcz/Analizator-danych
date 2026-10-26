from analiza import podstawowe_statystyki

import pandas as pd

#tworzymy zbiór (obiekt dataframe)

def test_podstawowe_statystyki(capsys):
    df = pd.DataFrame({
        "temp_max":[20,24],
        "temp_min":[10,12],
        "opady":[2,4]
    })

    podstawowe_statystyki(df)

    # capsys - przechwytuje tekst, który funkcja wypisuje za pomocą print()
    # capsys.readouter().out pobiera przechywcony tekst
    wynik = capsys.readouterr().out

    #assert sprawdza czy tekst zawiera oczekiwane wartości

    assert "Średnia temp maksymlana: 22.00 ℃" in wynik
    assert "Średnia temp minimalna: 11.00 ℃" in wynik
    assert "Suma opadów: 6.00 mm" in wynik


def test_brak_danych(capsys):
    podstawowe_statystyki(None)
    wynik = capsys.readouterr().out

    assert "Najpierw wczytaj dane z pliku csv" in wynik
    pass

def test_pusty_dataframe(capsys):
    df = pd.DataFrame()
    podstawowe_statystyki(df)
    wynik = capsys.readouterr().out

    assert "Najpierw wczytaj dane z pliku csv" in wynik
    pass