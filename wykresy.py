#generowanie wykresów
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored

# import numpy as np


def generuj_wykres(df):
    """
    Generuje wykres na podstawie danych

    Args:
        df (pandas.DataFrame | None): Dane wykorzystywae do wykresu
    """

    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku csv","red"))
        return

    dane = df.copy()

    dane["data"] = pd.to_datetime(dane["data"])

    fig, ax = plt.subplots()

    for miasto, pomiary in dane.groupby("miasto"):
        pomiary = pomiary.sort_values("data")

    ax.plot(pomiary["data"],pomiary["temp_max"],label = miasto)
    ax.set_title("Temp maksymalna")
    ax.set_xlabel("Data")
    ax.set_ylabel("Temperatura")
    ax.legend()
    ax.grid(True, color="#dddd",linestyle="-.")
    fig.autofmt_xdate()

    #zapis do pliku

    folder = Path("results")
    folder.mkdir(exist_ok=True)

    nazwa = f"Wykres_{dane["data"].min():%Y%m}.png"
    sciezka = folder / nazwa

    fig.savefig(sciezka)

    if os.path.exists(sciezka):
        print(colored("Zapisano wykres","green"))
    else:
        print(colored("Nie udało się zapisać wykresu","red"))
    
    plt.show()

