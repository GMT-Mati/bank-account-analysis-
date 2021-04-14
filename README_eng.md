# bank-account-analysis-
A program for analyzing your own budget, showing a list of transactions, the sum of incomes and expenses.
The program is under development, currently working on improving descriptions and data visualization.
Presentation of dependencies between various variables.
Update coming soon.

Soon a .csv file with sample data that can be worked on, the present one contains sensitive personal data that I need to delete first.

# Preparation:
The idea was born as a need to analyze your own finances, track them, control them and plan savings and future expenses.
The tools provided by the bank turned out to be insufficient and excel to be tedious to use.

# Program development process and difficulties encountered along the way:
1. I started by downloading my transaction history from the bank. I downloaded pdf by default and wasted a lot of time trying to use it. Ultimately, it turned out that the bank also provides the .csv entry
2. Then I started the key element of processing and organizing the collected data.
3. Receiving pandas.errors.ParserError: Error tokenizing data. C error I tried to fix with encoding = 'utf-8' and error_bad_lines = False, but it deleted some lines. Finally, the solution was very simple, it was enough to enter delimiter = ';' as reading conditions.
4. In the 'Transaction amount' column, there is a problem with replacing the type object with float. Trying with astype or Series.to_numeric fails, adding errors = 'coerce' changes all str to NaN. The solution is df.Series.str.replace, first e.g. string 1,000.00 to 1,000.00 with - ('', '') - to remove the space in str, then convert 1,000.00 to 1,000.00 - (' , ','. ') - to change comma to period and str to float. The complement is the pd.to_numeric function which changes the type object to float.
5. Changing the date in the 'Posting date' and 'Value date' columns from Object type to datetime using pd.Series.to_datetime
6. There was a problem with the incorrect change of the date, when the day of the month was in the range 13-31, the conversion was correct, while when the day of the month was in the range 1-12 then the program replaced the value of 'day' with 'month' by which instead of e.g. 2021-04-11 (eleventh of April) received 2021-11-04 (fourth of November). Problem solved with dayfirst = True.
7. After processing the data, I started writing the code. I started to create a Transactions class which by default will hold all possible options for our data.
8. The first option was to create a function that displays a list of transactions in a given month or year. The problem that arose here was the lack of clarity about the month in which we are talking about, so the latest one was always displayed. The error was quickly fixed using the lambda function: time (time.year, time.month) where the year and month were mapped as tuple, so you could select transactions from any month.
9. Addition of a function that displays transactions in any period of time. The condition inclusive = True allowed to include the start date in the search as well.
10. Another element was to create a function displaying the list of receipts, the list of expenses and the sum of these transactions. Everything can be broken down into annual, monthly or any time periods.
11. Creation of the info () function which allows to display all the data of interest to us in one simple command.

# Future update:
The closest elements I will work on are:
- clarifying what information I want to be displayed
- division into basic info and more precise ones
- adding visualization and graphical presentation of the data
- financial analysis for the presented data
- implementation of the ML process predicting the financial trend in a specific time period 
