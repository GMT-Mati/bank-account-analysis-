The original data contained numerous errors and inaccuracies. They were also in Polish. And they were not suitable for a publication because they contained sensitive data like names, credit card numbers and other.
In order to prepare the .csv file for publication, I performed the following steps: 
df = pd.read_csv(list_of_operations.csv', delimiter=';') # need 

df = df.rename({'Data księgowania': 'Posting Date', 'Nadawca / Odbiorca': 'Sender/Reciver',
                'Rachunek docelowy': 'Account', 'Tytułem': 'Title', 'Kwota operacji': 'Amount', 'Waluta': 'Currency',
                'Typ operacji': 'Type', 'Kategoria': 'Category'}, axis=1)
                
df['Account'] = df['Account'].str.replace(' ', '')
df['Account'] = df['Account'].str.replace(',', '.')
df['Account'] = pd.to_numeric(df['Account'])
df['Posting Date'] = pd.to_datetime(df['Posting Date'], dayfirst=True)

del df['Data waluty']
del df['Rachunek źródłowy']
del df['Numer referencyjny']
