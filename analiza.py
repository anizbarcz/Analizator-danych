#statystyki opisowe

def podstawowe_statystyki(df):
    """
    Oblicza i wyświetla podstawowe statystyki danych pogodowych
    
    Args:
        df(pandas.DataFrame | None)
            Dane zawierające tempertaury, wilgotoność i opady

    Returns:
        None: Funkcja wyświetla wyniki w konsoli 
    """

    if df is None or df.empty:
        print("Najpierw wczytaj dane z pliku csv")
        return

    print("\n***** PODSTAWOWE STATYSTYKI *****")

    print(f"Średnia temp maksymlana: {df['temp_max'].mean():.2f} ℃")
    print(f"Średnia temp minimalna: {df['temp_min'].mean():.2f} ℃")
    print(f"Suma opadów: {df['opady'].sum():.2f} mm")

# print(podstawowe_statystyki.__doc__)
# print(help(podstawowe_statystyki))