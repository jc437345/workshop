__author__ = 'jc437345'
"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

income = []
num_of_months = int(input("How many num_of_months? "))
def main():



    for month in range(1, num_of_months + 1):
        income = float(input("Enter income for month  {} : ".format(month)))
        incomes.append(income)
def func():
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
func()
print("=====")

"""

def same_firt_last(l):
    return l[0] == l[-1]
"""
