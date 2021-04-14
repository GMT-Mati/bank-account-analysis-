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
    def liczba_transakcji_rok(year):
        if year in range(3000):
            df['Year'] = df['Data księgowania'].apply(lambda time: time.year)
            print(f"Rok: {year}\n{df[df['Year'] == year].count().iloc[[0, 4, 6]]}")

    @staticmethod
    def liczba_transakcji_miesięcznie(year, month):
        if month in range(1, 13):
            df['Month'] = df['Data księgowania'].apply(lambda time: (time.year, time.month))
            
            def nazwa_miesiąca(month):
                return {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec',
                        8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'}[month]

            print(f"Miesiąc: {nazwa_miesiąca(month)}\n{df[df['Month'] == (year, month)].count().iloc[[0, 4, 6]]}")

    @staticmethod
    def liczba_transakcji_okres(start_date, end_date):
        df['Time'] = df['Data księgowania'].between(start_date, end_date, inclusive=True)
        print(f"Okres od {start_date} do {end_date}:\n{df.loc[df['Time']].count().iloc[[0, 4, 6]]}")

    @staticmethod
    def przychody_wydatki_roczne(year):
        df['Year'] = df['Data księgowania'].apply(lambda time: time.year)
        wykaz_dochodów = df.loc[(df['Year'] == year) &
                                (df['Kwota operacji'] > 0)][['Data księgowania', 'Kwota operacji']]
        wykaz_wydatków = df.loc[(df['Year'] == year) &
                                (df['Kwota operacji'] < 0)][['Data księgowania', 'Kwota operacji']]
        suma_dochodów = round(df.loc[(df['Year'] == year) & (df['Kwota operacji'] > 0)]['Kwota operacji'].sum(), 2)
        suma_wydatków = round(df.loc[(df['Year'] == year) & (df['Kwota operacji'] < 0)]['Kwota operacji'].sum(), 2)
        print(f"Rok: {year}\n{wykaz_dochodów}\nSuma dochodów: {suma_dochodów} zł")
        print(f"Rok: {year}\n{wykaz_wydatków}\nSuma wydatków: {suma_wydatków} zł")

    @staticmethod
    def przychod_wydatki_miesięczne(year, month):
        if month in range(1, 13):
            df['Month'] = df['Data księgowania'].apply(lambda time: (time.year, time.month))

            def nazwa_miesiąca(month):
                return {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec',
                        8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'}[month]

            wykaz_dochodów = df.loc[(df['Month'] == (year, month)) & (df['Kwota operacji'] > 0)][
                ['Data księgowania', 'Kwota operacji']]
            wykaz_wydatków = df.loc[(df['Month'] == (year, month)) & (df['Kwota operacji'] < 0)][
                ['Data księgowania', 'Kwota operacji']]
            suma_dochodów = round(df.loc[(df['Month'] == (year, month)) &
                                         (df['Kwota operacji'] > 0)]['Kwota operacji'].sum(), 2)
            suma_wydatków = round(df.loc[(df['Month'] == (year, month)) &
                                         (df['Kwota operacji'] < 0)]['Kwota operacji'].sum(), 2)
            print(f"Miesiąc: {nazwa_miesiąca(month)}\n{wykaz_dochodów}\nSuma dochodów: {suma_dochodów} zł")
            print(f"Miesiąc: {nazwa_miesiąca(month)}\n{wykaz_wydatków}\nSuma wydatków: {suma_wydatków} zł")
            
    @staticmethod
    def przychód_wydatki_okres(start_date, end_date):
        df['Time'] = df['Data księgowania'].between(start_date, end_date, inclusive=True)
        wykaz_dochodów = df.loc[(df['Time']) & (df['Kwota operacji'] > 0)][['Data księgowania', 'Kwota operacji']]
        wykaz_wydatków = df.loc[(df['Time']) & (df['Kwota operacji'] < 0)][['Data księgowania', 'Kwota operacji']]
        suma_dochodów = round(df.loc[(df['Time']) & (df['Kwota operacji'] > 0)]['Kwota operacji'].sum(), 2)
        suma_wydatków = round(df.loc[(df['Time']) & (df['Kwota operacji'] < 0)]['Kwota operacji'].sum(), 2)
        print(f"Okres od {start_date} do {end_date}:\n{wykaz_dochodów}\nSuma dochodów: {suma_dochodów} zł")
        print(f"Okres od {start_date} do {end_date}:\n{wykaz_wydatków}\nSuma wydatków: {suma_wydatków} zł")
        
    @staticmethod    
    def roczne_info(year):
        Transakcje.przychody_wydatki_roczne(year)
        Transakcje.liczba_transakcji_rok(year)
        
    @staticmethod
    def miesięczne_info(year, month):
        Transakcje.przychod_wydatki_miesięczne(year, month)
        Transakcje.liczba_transakcji_miesięcznie(year, month)
        
    @staticmethod
    def okresowe_info(start_date, end_date):
        Transakcje.przychód_wydatki_okres(start_date, end_date)
        Transakcje.liczba_transakcji_okres(start_date, end_date)

# przykładowe dane              
Transakcje.roczne_info(2021)
Transakcje.miesięczne_info(2020, 11)
Transakcje.okresowe_info('2020-12-24', '2021-2-14')              
