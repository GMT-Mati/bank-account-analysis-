# bank-account-analysis-
Program do analizy własnego budżetu, pokazujący listę transakcji, sumę wpływów i wydatków. Program w trakcie tworzenia, obecnie praca nad usprawnieniem opisów oraz wizualizacją danych. Prezentacji zależności między różnymi zmiennymi. Update wkrótce. Wkrótce plik .csv z przykładowymi danymi na których można pracować, obecny zawiera dane wrażliwe które muszę najpierw usunąć.

# Przygotowanie:
Pomysł zrodził się jako potrzeba do analizy własnych finansów, śledzenia ich, kontroli oraz planowania oszczędności i przyszłych wydatków. Narzędzia dostarczane przez bank okazały sie niewystarczająca, a excel mozolny w użytkowaniu.

# Przebieg tworzenia programu i napotkane po drodze trudności:
1. Zacząłem od pobrania historii transakcji z banku. Domyślenie pobrałem pdf i straciłem sporo czasu na próbach jego wykorzystania.      Ostatecznie okazałao się, że bank udostępnia też zapis .csv
2. Pojawiający się błąd pandas.errors.ParserError: Error tokenizing data. C error który próbowałem naprawić poprze encoding='utf-8' oraz error_bad_lines=False, jednak powodowało to usunięcie części linii. Finalnie rozwiązanie było banalnie proste, wystarczyło wprowadzić jako warunke czytania tekstu delimiter=';'
