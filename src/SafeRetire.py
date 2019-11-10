from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

class SafeRetire:
  def __init__(self, age, initialSalary, savingsInit, housingExpenseYrly, monthlyExpensesYrly, extraIncome, retirementAge, investPreference, initialInvestments):
    self.age = age
    self.initialSalary = initialSalary
    self.savingsInit = savingsInit
    self.housingExpenseYrly = housingExpenseYrly
    self.monthlyExpensesYrly = monthlyExpensesYrly
    self.extraIncome = extraIncome
    self.retirementAge = retirementAge
    self.investPreference = investPreference
    self.initialInvestments = initialInvestments
    
  def calculations(self):
    totalSavings = self.savingsInit
    totalInvestments = self.initialInvestments
    inflation = 0.983
    yearCounter = self.retirementAge - age
    salary = self.initialSalary
    investmentReturn = 1.10
    
    for i in range(yearCounter):
      yearlyExpenses = self.housingExpenseYrly + self.monthlyExpensesYrly
      yearlyTaxes = self.salary * self.taxBracket(salary);
      currentYearSavings = (self.salary - yearlyTaxes) + (self.totalSavings - yearlyExpenses) + extraIncome
      currentYearSavings =- self.currentYearInvestments
      currentYearInvestments = self.investPreference - currentYearSavings
      totalSavings = currentYearSavings * inflation
      totalInvestments = (totalInvestments - investmentReturn) + currentYearInvestments
      salary = salary * 1.045
    
    return totalSavings + totalInvestments
      
  def taxBracket(self):  
    if(salary  > 510301):
      return 0.37
    elif(salary > 204101):
      return 0.35
    elif(salary > 160725):
      return 0.32
    elif(salary > 84200):
      return 0.24
    elif(salary > 39475):
      return 0.12
    else:
      return 0.1


root = Tk()
app = Application(root)
root.mainloop()

#inputs
age = input("Enter your age: ")
salary = input("Enter your salary: ")
savings = input("Enter your initial savings: ")
investmentsBool = input("Do you have any investments? (Y/ N)")
if(investmentsBool == 'Y' or investmentsBool == 'y'):
  investmentsBool = True
else:
  investmentsBool = False
if(investmentsBool == True):
    investmentsInitial = input("Enter your total amount of money in investments: ")
    investmentPreference = input("Enter your investment preference as a percentage: ") * 0.01
housingExpense = input("Enter your monthly housing expenses: ") * 12
monthlyExpenseYrly = input("Do you have any other monthly expenses?: ")
extraIncome = input("Enter any extra income: ")
retireAge = input("At what age would you like to retire? ")
#end inputs

obj = SafeRetire(age, salary, savings, housingExpense, monthlyExpenseYrly, extraIncome, retireAge, investmentPreference, investmentsInitial)
print(obj.calculations())
