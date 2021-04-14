import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# zebranie i przygotowanie danych

# 1. pobranie pliku pdf z banku i konwersja na csv
# 2. pojawiający się błąd: pandas.errors.ParserError: Error tokenizing data. C error
#    próba naprawy poprzez encoding='utf-8', error_bad_lines=False, które powodowało usuwanie części linii
#    ostatecznym rozwiazaniem okazało się delimiter=';'
# 3. w kolumnie 'Kwota operacji' problem z zamianem typu object na float. próba poprzes astype czy Series.to_numeric
#    nie daje rezultatu, dodanie errors='coerce' zmienia wszsystkie str na Nan
#    rozwiązaniem jest df.Series.str.replace, najpierw str 1 000,00 na 1000,00(' ','') aby usunąć spację w str,
#    następnie zamiana 1000,00 na 1000.00(',','.') aby zmienić przecinek na kropkę i str na float
#    dopełnieniem jest funkcja pd.to_numeric zmieniająca typ object na float
# 4. zmiana daty z typu object na datatime za pomocą pd.Series.to_datatime,
#    pojawił się poblem z błędną zaminą dnia < 12 na miesiąc, naprawione przez dodanie parametru dayfirst=True

# zabiearanie i przetwarzanie danych

df = pd.read_csv('Lista_operacji_20210413_185554.csv', delimiter=';')  # 1, 2
df['Kwota operacji'] = df['Kwota operacji'].str.replace(' ', '')  # 3
df['Kwota operacji'] = df['Kwota operacji'].str.replace(',', '.')  # 3
df['Kwota operacji'] = pd.to_numeric(df['Kwota operacji'])  # 4
df['Data księgowania'] = pd.to_datetime(df['Data księgowania'], dayfirst=True)  # 4
df['Data waluty'] = pd.to_datetime(df['Data waluty'], dayfirst=True)  # 4



# 5. Liczba transakcji w danym miesiącu lub roku
# 6. Rozwinąć funkcję o wybór konkretnego roku i miesiąca
# 7. Pierwotnie pojawił się problem z wyborem miesiaca w konkretnym roku, rozwiazany poprzez stworzenei funkcji
#    lambda: time (time.year, time.month) gdzie rok i miesiac zostały zmapowane jako tuple
# 8. Dodanie funkcji wyboru transakcji w określonym czasie
# 9. Funkcja zwracająca listę wpływów, wydatków oraz ich sumę w rozliczeniu rocznym, miesiecznym i dowolnym okresie


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


# print(df.columns)
# # print(df.info())
# # print(df['Kategoria'].value_counts())
# print()
# print(df['Kategoria'].value_counts())
print(df.columns)
print(df['Nadawca / Odbiorca'].value_counts())

# wykaz kategorii transakcji,
Transakcje.roczne_info(2021)
Transakcje.miesięczne_info(2020, 11)
Transakcje.okresowe_info('2020-12-24', '2021-2-14')