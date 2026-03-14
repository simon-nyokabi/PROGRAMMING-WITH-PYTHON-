# list of mixed payments
transactions = [1200, -200, 3500, -50, 450, -120, 1000]
#Get the income list and the totals from the transactions
#income_list = [income for income in transactions if income > 0] # used list comprehensioons
income_list = list(filter(lambda x :x > 0, transactions))

total_income = sum(income_list)

#getting the taxes which is  15% per income
taxes_list = list(map(lambda x: x * 0.15, income_list ))
total_taxes = sum(taxes_list)

#Getting the expenses 
expense_list = [abs(expense) for expense in transactions if expense < 0 ] # list comprehensions
total_spent = sum(expense_list) + total_taxes

#printing the invoice
summary = (
    f'\nTotal Earned : $ {total_income: ,.2f}'
    f'\nTotal Taxes : $ {total_taxes: ,.2f}'
    f'\nTotal spent : $ {total_spent: ,.2f}'
    f'\nTake Home : $ {total_income - total_spent: ,.2f}'
)
print(summary)




