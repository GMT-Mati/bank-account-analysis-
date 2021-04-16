import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# FOR MORE INFORMATION PLEASE SEE THE DOCUMENTATION
# COLLECTING AND PREPARING DATA

df = pd.read_csv('list_of_operations.csv', delimiter=',')
df['Amount'] = pd.to_numeric(df['Amount'])  # 4
df['Posting Date'] = pd.to_datetime(df['Posting Date'], dayfirst=True)

# PROCESSING DATA


class AllData:

    def __init__(self, year, month, start_date, end_date):
        self.Transaction = self.Transaction()
        self.year = year
        self.month = month
        self.start_date = start_date
        self.end_date = end_date
        
    class Transaction:
        
        @staticmethod
        def annual_tr(year):
            df['Year'] = df['Posting Date'].apply(lambda time: time.year)
            income_list = df.loc[(df['Year'] == year) & (df['Amount'] > 0)][['Amount', 'Posting Date', 'Category']]
            expenses_list = df.loc[(df['Year'] == year) & (df['Amount'] < 0)][['Amount', 'Posting Date', 'Category']]
            income_sum = round(df.loc[(df['Year'] == year) & (df['Amount'] > 0)]['Amount'].sum(), 2)
            expenses_sum = round(df.loc[(df['Year'] == year) & (df['Amount'] < 0)]['Amount'].sum(), 2)
            income_num_tr = len(df.loc[(df['Year'] == year) & (df['Amount'] > 0)]['Amount'])
            expenses_num_tr = len(df.loc[(df['Year'] == year) & (df['Amount'] < 0)]['Amount'])
            profit = round(income_sum + expenses_sum, 2)
            print(f"In year {year}, {df[df['Year'] == year].count().iloc[0]} transactions were carried out.\n"
                  f"Total income: {income_sum} USD ({income_num_tr} transactions)"
                  f"\nTotal expenses: {expenses_sum} USD ({expenses_num_tr} transactions)")
            if profit > 0:
                print(f"Total profit: {profit} USD\n")
            else:
                print(f"Total loss: {profit} USD\n")
            print(f"List of income in {year}:\n{income_list.to_string(index=False)}\n")
            print(f"List of expenses in {year}:\n{expenses_list.to_string(index=False)}\n")

        @staticmethod
        def monthly_tr(year, month):
            df['Month'] = df['Posting Date'].apply(lambda time: (time.year, time.month))

            def month_name(month):
                return {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                        8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[month]

            income_list = df.loc[(df['Month'] == (year, month)) & (df['Amount'] > 0)][
                ['Amount', 'Posting Date', 'Category']]
            expenses_list = df.loc[(df['Month'] == (year, month)) & (df['Amount'] < 0)][
                ['Amount', 'Posting Date', 'Category']]
            income_sum = round(df.loc[(df['Month'] == (year, month)) & (df['Amount'] > 0)]['Amount'].sum(), 2)
            expenses_sum = round(df.loc[(df['Month'] == (year, month)) & (df['Amount'] < 0)]['Amount'].sum(), 2)
            income_num_tr = len(df.loc[(df['Month'] == (year, month)) & (df['Amount'] > 0)]['Amount'])
            expenses_num_tr = len(df.loc[(df['Month'] == (year, month)) & (df['Amount'] < 0)]['Amount'])
            profit = round(income_sum + expenses_sum, 2)
            print(f"In {month_name(month)} {year}, {df[df['Month'] == (year, month)].count().iloc[0]} "
                  f"transactions were carried out.\n"
                  f"Total income: {income_sum} USD ({income_num_tr} transactions)"
                  f"\nTotal expenses: {expenses_sum} USD ({expenses_num_tr} transactions)")
            if profit > 0:
                print(f"Total profit: {profit} zł\n")
            else:
                print(f"Total loss: {profit} zł\n")
            print(f"List of income for {month_name(month)} {year}: \n{income_list.to_string(index=False)}\n")
            print(f"List of expenses for {month_name(month)} {year}:\n{expenses_list.to_string(index=False)}\n")

        @staticmethod
        def periodic_tr(start_date, end_date):
            df['Time'] = df['Posting Date'].between(start_date, end_date, inclusive=True)
            income = df.loc[(df['Time']) & (df['Amount'] > 0)][
                ['Amount', 'Posting Date', 'Category']]
            expenses_list = df.loc[(df['Time']) & (df['Amount'] < 0)][
                ['Amount', 'Posting Date', 'Category']]
            income_sum = round(df.loc[(df['Time']) & (df['Amount'] > 0)]['Amount'].sum(), 2)
            expenses_sum = round(df.loc[(df['Time']) & (df['Amount'] < 0)]['Amount'].sum(), 2)
            income_num_tr = len(df.loc[(df['Time']) & (df['Amount'] > 0)]['Amount'])
            expenses_num_tr = len(df.loc[(df['Time']) & (df['Amount'] < 0)]['Amount'])
            profit = round(income_sum + expenses_sum, 2)
            print(
                f"From {start_date} to {end_date}, {df.loc[df['Time']].count().iloc[0]} transactions were carried out.\n"
                f"Total income: {income_sum} zł ({income_num_tr} transactions)\n"
                f"Total expenses: {expenses_sum} zł ({expenses_num_tr} transactions)")
            if profit > 0:
                print(f"Total profit: {profit} zł\n")
            else:
                print(f"Total loss: {profit} zł\n")
            print(f"List of income fom {start_date} to {end_date}:\n{income.to_string(index=False)}\n")
            print(f"List of expenses from {start_date} to {end_date}:\n{expenses_list.to_string(index=False)}\n")

    class Salary:
      
        @staticmethod
        def annual(year):
            df['Year'] = df['Posting Date'].apply(lambda time: time.year)
            salary_list = df[(df['Year'] == year) & (df['Title'] == 'Salary')][
                ['Posting Date', 'Sender/Receiver', 'Amount']]
            salary_value = df[(df['Year'] == year) & (df['Title'] == 'Salary')]['Amount']
            employer = df[(df['Year'] == year) & (df['Title'] == 'Salary')]['Sender/Receiver']
            print(f"\nSalary list in {year}:\n{salary_list}\n")
            print(f"Lowest salary in {year}:\n{salary_list.min()}\n")
            print(f"Highest salary in {year}:\n{salary_list.max()}\n")
            print(f'Average salary in {year}: {round(salary_value.mean(), 2)} USD\n')
            print(f"Employer(s) in {year}: {', '.join(list(set(employer)))}")

        @staticmethod
        def monthly(year, month):
            df['Month'] = df['Posting Date'].apply(lambda time: (time.year, time.month))

            def month_name(month):
                return {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                        8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[month]

            salary_list = df[(df['Month'] == (year, month)) & (df['Title'] == 'Salary')][
                ['Posting Date', 'Sender/Receiver', 'Amount']]
            salary_value = df[(df['Month'] == (year, month)) & (df['Title'] == 'Salary')]['Amount']
            employer = df[(df['Month'] == (year, month)) & (df['Title'] == 'Salary')]['Sender/Receiver']
            print(f"\nSalary list in {month_name(month)} {year}:\n{salary_list}\n")
            print(f"Lowest salary in {month_name(month)} {year}:\n{salary_list.min()}\n")
            print(f"Highest salary in {month_name(month)} {year}:\n{salary_list.max()}\n")
            print(f'Average salary in {month_name(month)} {year}: {round(salary_value.mean(), 2)} USD\n')
            print(f"Employer(s) in {month_name(month)} {year}: {', '.join(list(set(employer)))}")

        @staticmethod
        def periodic(start_date, end_date):
            df['Time'] = df['Posting Date'].between(start_date, end_date, inclusive=True)
            salary_list = df.loc[(df['Time']) & (df['Title'] == 'Salary')][
                ['Posting Date', 'Sender/Receiver', 'Amount']]
            salary_value = df.loc[(df['Time']) & (df['Title'] == 'Salary')]['Amount']
            employer = df.loc[(df['Time']) & (df['Title'] == 'Salary')]['Sender/Receiver']
            print(f"\nSalary list from {start_date} to {end_date}:\n{salary_list}\n")
            print(f"Lowest salary from {start_date} to {end_date}:\n{salary_list.min()}\n")
            print(f"Highest salary from {start_date} to {end_date}:\n{salary_list.max()}\n")
            print(f'Average salary from {start_date} to {end_date}: {round(salary_value.mean(), 2)} USD\n')
            print(f"Employer(s) from {start_date} to {end_date}: {', '.join(list(set(employer)))}")

    class Information:

        @staticmethod
        def annual(year):
            AllData.Transaction.annual_tr(year)

        @staticmethod
        def monthly(year, month):
            AllData.Transaction.monthly_tr(year, month)

        @staticmethod
        def periodic(start_date, end_date):
            AllData.Transaction.periodic_tr(start_date, end_date)


# FOR EXAMPLE                  
AllData.Transaction.annual_tr(2021)
AllData.Salary.monthly(2020, 11)
AllData.Information.periodic('2021-1-12', '2021-4-12')
