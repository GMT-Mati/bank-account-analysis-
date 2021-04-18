import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from decimal import Decimal

# COLLECTING AND PREPARING DATA

df = pd.read_csv('list_of_operations.csv', delimiter=',')
df['Amount'] = pd.to_numeric(df['Amount'])
df['Posting Date'] = pd.to_datetime(df['Posting Date'], dayfirst=True)

# PROCESSING DATA


class AllData:

    def __init__(self, year, month, start_date, end_date):

        self.Transaction = self.Transaction()
        self.year = year
        self.month = month
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def month_name(month):

        return {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}[month]

    @staticmethod
    def year_date():

        df['Year'] = df['Posting Date'].apply(lambda time: time.year)

    @staticmethod
    def period_date(start_date, end_date):

        df['Time'] = df['Posting Date'].between(start_date, end_date, inclusive=True)

    @staticmethod
    def month_date(year):

        df['Month'] = df['Posting Date'].apply(lambda time: (time.year, time.month))

    class Transaction:

        @staticmethod
        def annual_tr(year):

            AllData.year_date()
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

            AllData.month_date(year)
            AllData.month_name(month)
            income_list = df.loc[(df['Month'] == (year, month)) & (df['Amount'] > 0)][
                ['Amount', 'Posting Date', 'Category']]
            expenses_list = df.loc[(df['Month'] == (year, month)) & (df['Amount'] < 0)][
                ['Amount', 'Posting Date', 'Category']]
            all_trans = df.loc[df['Month'] == (year, month)][['Amount', 'Posting Date', 'Category']]
            income_sum = round(df.loc[(df['Month'] == (year, month)) & (df['Amount'] > 0)]['Amount'].sum(), 2)
            expenses_sum = round(df.loc[(df['Month'] == (year, month)) & (df['Amount'] < 0)]['Amount'].sum(), 2)
            income_num_tr = len(df.loc[(df['Month'] == (year, month)) & (df['Amount'] > 0)]['Amount'])
            expenses_num_tr = len(df.loc[(df['Month'] == (year, month)) & (df['Amount'] < 0)]['Amount'])
            profit = round(income_sum + expenses_sum, 2)
            print(f"In {AllData.month_name(month)} {year}, {df[df['Month'] == (year, month)].count().iloc[0]} "
                  f"transactions were carried out.\n"
                  f"Total income: {income_sum} USD ({income_num_tr} transactions)"
                  f"\nTotal expenses: {expenses_sum} USD ({expenses_num_tr} transactions)")
            if profit > 0:
                print(f"Total profit: {profit} zł\n")
            else:
                print(f"Total loss: {profit} zł\n")
            print(f"List of income for {AllData.month_name(month)} {year}: \n{income_list.to_string(index=False)}\n")
            print(f"List of expenses for {AllData.month_name(month)} {year}:\n{expenses_list.to_string(index=False)}\n")
            print(all_trans)

        @staticmethod
        def periodic_tr(start_date, end_date):

            AllData.period_date(start_date, end_date)
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
                f"From {start_date} to {end_date}, {df.loc[df['Time']].count().iloc[0]} "
                f"transactions were carried out.\n"
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
            AllData.year_date()
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
            AllData.month_date(year)
            AllData.month_name(month)
            salary_list = df[(df['Month'] == (year, month)) & (df['Title'] == 'Salary')][
                ['Posting Date', 'Sender/Receiver', 'Amount']]
            salary_value = df[(df['Month'] == (year, month)) & (df['Title'] == 'Salary')]['Amount']
            employer = df[(df['Month'] == (year, month)) & (df['Title'] == 'Salary')]['Sender/Receiver']
            print(f"\nSalary list in {AllData.month_name(month)} {year}:\n{salary_list}\n")
            print(f"Lowest salary in {AllData.month_name(month)} {year}:\n{salary_list.min()}\n")
            print(f"Highest salary in {AllData.month_name(month)} {year}:\n{salary_list.max()}\n")
            print(f'Average salary in {AllData.month_name(month)} {year}: {round(salary_value.mean(), 2)} USD\n')
            print(f"Employer(s) in {AllData.month_name(month)} {year}: {', '.join(list(set(employer)))}")

        @staticmethod
        def periodic(start_date, end_date):
            AllData.period_date(start_date, end_date)
            salary_list = df.loc[(df['Time']) & (df['Title'] == 'Salary')][
                ['Posting Date', 'Sender/Receiver', 'Amount']]
            salary_value = df.loc[(df['Time']) & (df['Title'] == 'Salary')]['Amount']
            employer = df.loc[(df['Time']) & (df['Title'] == 'Salary')]['Sender/Receiver']
            print(f"\nSalary list from {start_date} to {end_date}:\n{salary_list}\n")
            print(f"Lowest salary from {start_date} to {end_date}:\n{salary_list.min()}\n")
            print(f"Highest salary from {start_date} to {end_date}:\n{salary_list.max()}\n")
            print(f'Average salary from {start_date} to {end_date}: {round(salary_value.mean(), 2)} USD\n')
            print(f"Employer(s) from {start_date} to {end_date}: {', '.join(list(set(employer)))}")

    class Purchase:
        # all expenses that are not, for example taxes, fees, insurances etc.
        # in no category, decided to iterate through type and title
        @staticmethod
        def annual(year):

            AllData.year_date()
            purchase_list = df.loc[(df['Year'] == year) &
                                   ((df['Category'] == 'Groceries') | (df['Category'] == 'Cosmetics') |
                                    (df['Category'] == 'Fuel') | (df['Category'] == 'Clothes') |
                                    (df['Category'] == 'Equipment') |
                                    (df['Category'] == 'Clothes') | (df['Category'] == 'Footwear') |
                                    (df['Category'] == 'Acessories and Jewelry') | (df['Category'] == 'Garden') |
                                    (df['Category'] == 'Online Shopping') |
                                    (df['Category'] == 'Newspapers and Magazines') |
                                    (df['Category'] == 'Books') | (df['Category'] == 'Sport') |
                                    (df['Category'] == 'Cinema and Theater') |
                                    (df['Category'] == 'Glasses and Lenses') | (df['Category'] == 'Toys') |
                                    (df['Category'] == 'Restaurant and Cafes') |
                                    (df['Category'] == 'Car wash, inspections and repairs') |
                                    (df['Category'] == 'Medicine') | (df['Category'] == 'Repairs and Renovations') |
                                    (df['Category'] == 'Beauty, Hairdresser and Beautician') |
                                    (df['Sender/Receiver'] == 'Bus Station') | (df['Sender/Receiver'] == 'PayPal') |
                                    (df['Sender/Receiver'] == 'ShoeShop') | (df['Sender/Receiver'] == 'PayU') |
                                    (df['Sender/Receiver'] == 'Transfers24') |
                                    (df['Sender/Receiver'] == 'Car Parking') | (df['Sender/Receiver'] == 'Tesco') |
                                    (df['Sender/Receiver'] == 'Post Office') | (df['Category'] == 'Sale'))][
                ['Amount', 'Posting Date', 'Category']]
            print(f"\nNumber of purchases: {len(purchase_list)}\nList of all purchases:\n{purchase_list.to_string()}")
            l = []
            for item in df['Category']:
                l.append(item)
                print(item)
            print(set(l))
            
    class Car:

        @staticmethod
        def annual(year):
            AllData.year_date()
            car_expenses = df.loc[(df['Year'] == year) &
                                  ((df['Category'] == "Car wash, inspections and repairs") |
                                   (df['Category'] == 'Fuel'))][['Amount', 'Posting Date', 'Sender/Receiver']]
            car_wash = df.loc[(df['Year'] == year) & (df['Category'] == "Car wash, inspections and repairs")]
            gas_station = df.loc[(df['Year'] == year) & (df['Category'] == "Fuel")]
            mechanic_cost = round(df.loc[(df['Year'] == year) &
                              (df['Sender/Receiver'] == 'Mechanic')]['Amount'].sum(), 2)
            car_wash_cost = round(df.loc[(df['Year'] == year) &
                              (df['Sender/Receiver'] == 'Car Wash')]['Amount'].sum(), 2)
            gas_cost_bp = round(df.loc[(df['Year'] == year) &
                              (df['Sender/Receiver'] == 'BP')]['Amount'].sum(), 2)
            gas_cost_shell = round(df.loc[(df['Year'] == year) &
                              (df['Sender/Receiver'] == 'Shell')]['Amount'].sum(), 2)

            print(f"\nList of car expenses in {year}:\n{car_expenses}")
            print(f"\nDriver was {len(car_wash)} times in Car Wash or repairs a car.")
            print(f"On mechanic he spent {mechanic_cost} USD, and for Car Wash {car_wash_cost} USD.")
            print(f"\nList of gas station where driver refuel in {year}:"
                  f"\n{gas_station['Sender/Receiver'].value_counts().to_string()}")


        @staticmethod
        def monthly(year, month):
            AllData.year_date()
            car_expenses = df.loc[(df['Year'] == (year, month)) &
                                  ((df['Category'] == "Car wash, inspections and repairs") |
                                   (df['Category'] == 'Fuel'))][['Amount', 'Posting Date', 'Sender/Receiver']]
            print(car_expenses)

        @staticmethod
        def periodic(start_date, end_date):
            AllData.period_date(start_date, end_date)
            car_expenses = df.loc[df['Time'] & ((df['Category'] == "Car wash, inspections and repairs") |
                                                (df['Category'] == 'Fuel'))][
                ['Amount', 'Posting Date', 'Sender/Receiver']]
            print(car_expenses)

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


print(df.columns)
# print(df['Category'].value_counts())
# print(df[df['Category'] == 'No Category'][['Sender/Receiver', 'Title', 'Type']])
# AllData.Transaction.annual_tr(2021)
# AllData.Transaction.periodic_tr('2020-12-4', '2021-2-18')
# AllData.Salary.annual(2020)
# AllData.Salary.monthly(2021, 4)
# AllData.Salary.periodic('2020-12-4', '2021-2-18')
# AllData.Transaction.monthly_tr(2020, 11)
# print(AllData.Purchase.annual(2020))
AllData.Car.annual(2020)
# AllData.Car.periodic('2020-12-19', '2021-1-31')