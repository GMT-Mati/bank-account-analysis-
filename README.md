# bank-account-analysis-
Program do analizy własnego budżetu, pokazujący listę transakcji, sumę wpływów i wydatków. Program w trakcie tworzenia, obecnie praca nad usprawnieniem opisów oraz wizualizacją danych. Prezentacji zależności między różnymi zmiennymi. Update wkrótce. Wkrótce plik .csv z przykładowymi danymi na których można pracować, obecny zawiera dane wrażliwe które muszę najpierw usunąć.

# Przygotowanie:
Pomysł zrodził się jako potrzeba do analizy własnych finansów, śledzenia ich, kontroli oraz planowania oszczędności i przyszłych wydatków. Narzędzia dostarczane przez bank okazały sie niewystarczająca, a excel mozolny w użytkowaniu.

# Przebieg tworzenia programu i napotkane po drodze trudności:
1. Zacząłem od pobrania historii transakcji z banku. Domyślenie pobrałem pdf i straciłem sporo czasu na próbach jego wykorzystania.      Ostatecznie okazałao się, że bank udostępnia też zapis .csv
2. Następnie rozpocząłem kluczowy element przetwarzania i porzadkowania zebranych danych.
3. Pojawiający się błąd pandas.errors.ParserError: Error tokenizing data. C error który próbowałem naprawić poprzez encoding='utf-8'    oraz error_bad_lines=False, jednak powodowało to usunięcie części linii. Finalnie rozwiązanie było banalnie proste, wystarczyło      wprowadzić jako warunke czytania tekstu delimiter=';'
4. W kolumnie 'Kwota operacji' problem z zamianą typu object na float. Próba poprzez astype czy Series.to_numeric nie daje rezultatu,    dodanie errors='coerce' zmienia wszystkie str na NaN. Rozwiązaniem jest df.Series.str.replace, najpierw np. string 1 000,00 na        1000,00 za pomocą - (' ','') - aby usunąć spację w str, a następnie zamiana 1000,00 na 1000.00 - (',','.') - aby zmienić przecinek    na kropkę i str na float. Dopełnieniem jest funkcja pd.to_numeric zmieniająca typ object na float.
5. Zmiana daty w kolumnach 'Data księgowania' i 'Data waluty' z typu Object na datetime za pomocą pd.Series.to_datetime
6. Pojawił się problem z błędną zmianą daty, kiedy dzień miesiąca był z przedziału 13-31, zamiana była prawidłowa, natomiast kiedy      dzień miesiąca był z przedziału 1-12 wtedy program zamieniał wartość 'dzień' z 'miesiąc' przez co zamiast np. 2021-04-11(jedenasty    kwietnia) otrzymałem 2021-11-04(cztwart listopada). Problem rozwiązany przy pomocy dayfirst=True.
7. Po przetworzeniu danych rozpocząłem pisanie kodu. Zacząłem do stworzenia klasy Transakcje któa domyślnie będzie przechowywac          wszytkie możliwe opcje dla naszych danych.
8. Pierwszą możliwością było utworzenie funkcji która wyświetla listę transakcji w dancym miesiącu lub roku. Problem jaki się tu        pojawił było niedoprecyzowanie o miesiąc w którym roku nam chodzi, więc zawsze wyświetlany był ten najnowszy. Błąd udało się w        miarę szybko naprawić wykorzystując funkcję lambda: time (time.year, time.month) gdzie rok i miesiać zostały zmapowane jako tuple,    przez co można było wybrac transakcje z dowolnego miesiąca.
9. Dodanie funkcji wyświetlającej transakcje w dowolnym okresie czasu. Warunek inclusive=True pozwolił w wyszukiwanie włączyć także      datę początkową.
10. Kolejnym elemenetem było stworzenie funkcji wyświetlającej listę wpływów, listę wydatków oraz sumę tych transakcji. Wszystko        zyskało możliwość rozbicia na okresy roczne, miesiaczne lub w dowolnym przedziale czasu.
11. Utowrzenie funkcji info() która pozwala w jednym prostym poleceniu wyświetlić wszystkie interesujące nas dane.

# Przyszły update:
Najbliższe elementy nad którymi będę pracował to:
- doprecyzowanie jakie informacje chcę aby były wyświetlone
- podział na podtawowe info oraz te bardziej precyzyjne
- dodanie wizualizacji i graficzne przedstwienie danych
- analiza finansowa dla prezentowanych dancyh
- zainplementowanie procesu ML przewidującego trend finasowy w konkretnym przedziale czasu
