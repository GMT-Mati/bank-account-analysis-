import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# zabiearanie i przetwarzanie danych

df = pd.read_csv('Lista_operacj.csv', delimiter=';')  # 1, 2
df['Kwota operacji'] = df['Kwota operacji'].str.replace(' ', '')  # 3
df['Kwota operacji'] = df['Kwota operacji'].str.replace(',', '.')  # 3
df['Kwota operacji'] = pd.to_numeric(df['Kwota operacji'])  # 4
df['Data księgowania'] = pd.to_datetime(df['Data księgowania'], dayfirst=True)  # 4
df['Data waluty'] = pd.to_datetime(df['Data waluty'], dayfirst=True)  # 4

# klasa wyświetlająca transakcje, wypływy, wydatki w dowolnym okresie czasu


class Transakcje:

    def __init__(self, year, month, start_date, end_date):
        self.year = year
        self.month = month
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def przychody_wydatki_roczne(year):
        df['Year'] = df['Data księgowania'].apply(lambda time: time.year)
        wykaz_dochodow = df.loc[(df['Year'] == year) &
                                (df['Kwota operacji'] > 0)][['Kwota operacji', 'Data księgowania', 'Kategoria']]
        wykaz_wydatkow = df.loc[(df['Year'] == year) &
                                (df['Kwota operacji'] < 0)][['Kwota operacji', 'Data księgowania', 'Kategoria']]
        suma_dochodow = round(df.loc[(df['Year'] == year) & (df['Kwota operacji'] > 0)]['Kwota operacji'].sum(), 2)
        suma_wydatkow = round(df.loc[(df['Year'] == year) & (df['Kwota operacji'] < 0)]['Kwota operacji'].sum(), 2)
        ilosc_transakcji_przychodu = len(df.loc[(df['Year'] == year) & (df['Kwota operacji'] > 0)]['Kwota operacji'])
        ilosc_transakcji_wydatkow = len(df.loc[(df['Year'] == year) & (df['Kwota operacji'] < 0)]['Kwota operacji'])
        zysk = round(suma_dochodow + suma_wydatkow, 2)
        print(f"W roku: {year} przeprowadzono {df[df['Year'] == year].count().iloc[0]} transakcje.\n"
              f"Suma dochodów: {suma_dochodow} zł ({ilosc_transakcji_przychodu} transakcje)"
              f"\nSuma wydatków: {suma_wydatkow} zł ({ilosc_transakcji_wydatkow} transakcje)")
        if zysk > 0:
            print(f"Zysk wyniósł: {zysk} zł\n")
        else:
            print(f"Strata wyniosła: {zysk} zł\n")
        print(f"Dochody w roku {year} to:\n{wykaz_dochodow.to_string(index=False)}\n")
        print(f"Wydatki w roku {year} to:\n{wykaz_wydatkow.to_string(index=False)}\n")

    @staticmethod
    def przychod_wydatki_miesięczne(year, month):
        df['Month'] = df['Data księgowania'].apply(lambda time: (time.year, time.month))

        def nazwa_miesiąca(month):
            return {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec',
                    8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'}[month]

        wykaz_dochodow = df.loc[(df['Month'] == (year, month)) & (df['Kwota operacji'] > 0)][
            ['Kwota operacji', 'Data księgowania', 'Kategoria']]
        wykaz_wydatkow = df.loc[(df['Month'] == (year, month)) & (df['Kwota operacji'] < 0)][
            ['Kwota operacji', 'Data księgowania', 'Kategoria']]
        suma_dochodow = round(df.loc[(df['Month'] == (year, month)) &
                                     (df['Kwota operacji'] > 0)]['Kwota operacji'].sum(), 2)
        suma_wydatkow = round(df.loc[(df['Month'] == (year, month)) &
                                     (df['Kwota operacji'] < 0)]['Kwota operacji'].sum(), 2)
        ilosc_transakcji_przychodu = len(df.loc[(df['Month'] == (year, month)) &
                                                (df['Kwota operacji'] > 0)]['Kwota operacji'])
        ilosc_transakcji_wydatkow = len(df.loc[(df['Month'] == (year, month)) &
                                               (df['Kwota operacji'] < 0)]['Kwota operacji'])
        zysk = round(suma_dochodow + suma_wydatkow, 2)
        print(f"W miesiącu {nazwa_miesiąca(month)} {year} przeprowadzono: "
              f"{df[df['Month'] == (year, month)].count().iloc[0]} transakcje.\n"
              f"Suma dochodów: {suma_dochodow} zł ({ilosc_transakcji_przychodu} transakcje)"
              f"\nSuma wydatków: {suma_wydatkow} zł ({ilosc_transakcji_wydatkow} transakcje)")
        if zysk > 0:
            print(f"Zysk wyniósł: {zysk} zł\n")
        else:
            print(f"Strata wyniosła: {zysk} zł\n")
        print(f"Dochody w wybranym miesiącu to:\n{wykaz_dochodow.to_string(index=False)}\n")
        print(f"Wydatki w wybranym miesiącu to:\n{wykaz_wydatkow.to_string(index=False)}\n")
            
    @staticmethod
    def przychód_wydatki_okres(start_date, end_date):
        df['Time'] = df['Data księgowania'].between(start_date, end_date, inclusive=True)
        wykaz_dochodow = df.loc[(df['Time']) & (df['Kwota operacji'] > 0)][
            ['Kwota operacji', 'Data księgowania', 'Kategoria']]
        wykaz_wydatkow = df.loc[(df['Time']) & (df['Kwota operacji'] < 0)][
            ['Kwota operacji', 'Data księgowania', 'Kategoria']]
        suma_dochodow = round(df.loc[(df['Time']) & (df['Kwota operacji'] > 0)]['Kwota operacji'].sum(), 2)
        suma_wydatkow = round(df.loc[(df['Time']) & (df['Kwota operacji'] < 0)]['Kwota operacji'].sum(), 2)
        ilosc_transakcji_przychodu = len(df.loc[(df['Time']) & (df['Kwota operacji'] > 0)]['Kwota operacji'])
        ilosc_transakcji_wydatkow = len(df.loc[(df['Time']) & (df['Kwota operacji'] < 0)]['Kwota operacji'])
        zysk = round(suma_dochodow + suma_wydatkow, 2)
        print(f"W okresie od {start_date} do {end_date} przeprowadzono "
              f"{df.loc[df['Time']].count().iloc[0]} transakcje.\n"
              f"Suma dochodów: {suma_dochodow} zł ({ilosc_transakcji_przychodu} transakcje)\n"
              f"Suma wydatków: {suma_wydatkow} zł ({ilosc_transakcji_wydatkow} transakcje)")
        if zysk > 0:
            print(f"Zysk wyniósł: {zysk} zł\n")
        else:
            print(f"Strata wyniosła: {zysk} zł\n")
        print(f"Dochody w wybranym okresie to:\n{wykaz_dochodow.to_string(index=False)}\n")
        print(f"Wydatki w wybranym okresie to:\n{wykaz_wydatkow.to_string(index=False)}\n")


class Informacja:
    def __init__(self, year, month, start_date, end_date):
        self.year = year
        self.month = month
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def roczne(year):
        Transakcje.przychody_wydatki_roczne(year)

    @staticmethod
    def miesięczne(year, month):
        Transakcje.przychod_wydatki_miesięczne(year, month)

    @staticmethod
    def okresowe(start_date, end_date):
        Transakcje.przychód_wydatki_okres(start_date, end_date)
        
        
# przykładowe dane              
Informacja.roczne(2021)
Informacja.miesięczne(2020, 11)
Informacja.okresowe('2020-12-24', '2021-2-14')              
