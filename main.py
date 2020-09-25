"""
Week 2 - Python
This is the first of three programs designed to display 
a competent knowledge of Python.
This program in particular will evaulate a dinner bill including tips 
through several different means.
Functions, variables, expressions, loops, and other aspects 
of programming.
1. Asks the user for their bill amount
2. Asks the User how they'd like to tip - Percentage, waiter/waitress
quality, or manual entry.
3. Evaluates the tip
4. Evaluates the total cost
"""

def promptBillAmount():
   inputInvalid = True
   cost = 0.00
   while inputInvalid == True:
      try:
         cost = float(input("Please enter the cost of your bill: $"))
         inputInvalid = False
         cost = "{:.2f}".format(cost)
      except:
         print("Invalid Number. Please enter a specific amount. (Ex: $12.50)")

   return cost

def promptPercentage():
   inputInvalid = True
   percent = 0
   while inputInvalid == True:
      try:
         percent = int(input("Please enter the percentage of the tip you'd like to give (Whole numbers only): "))
         inputInvalid = False
      except:
         print("Invalid Number. Please provide only a whole number. (Ex: 20)")
   return percent

def ratingToPercent(rating):
   percentDic = {
      1: 5,
      2: 10,
      3: 15,
      4: 25,
      5: 35
   }
   return percentDic.get(rating, "Invalid")

def rateServer():
   inputInvalid = True
   rating = 0
   percent = 0
   while inputInvalid == True:
      try:
         rating = int(input("Please give your server a rating between 1 and 5 stars: "))
      except:
         print("Invalid rating.")
         continue
      if rating < 1 or rating > 5:
         print("Invalid rating.")
         continue
      percent = ratingToPercent(rating)
      acceptable = input("Is a " + str(percent) + "% tip okay? (Y/N)")
      if acceptable == "Y" or acceptable == "y" or acceptable == "Yes" or acceptable == "yes" or acceptable == "YES":
         inputInvalid = False
      else:
         continue

   return percent

def promptTipAmount():
   inputInvalid = True
   tip = 0.00
   while inputInvalid == True:
      try:
         tip = float(input("Please enter the amount you'd like to tip: $"))
         inputInvalid = False
         tip = "{:.2f}".format(tip)
      except:
         print("Invalid Number. Please enter a specific amount. (Ex: $4.25)")

   return tip

def getTip():
   tip = 0.20
   return tip

def calculateTotal(bill, tip):
   total = 0.00
   total = float(bill) + float(tip)
   return total

def displayTotal(total):
   total = "{:.2f}".format(total)
   print("Your total is $", total, ".", sep="")

bill = promptBillAmount()
tip = getTip()
total = calculateTotal(bill, tip)

displayTotal(total)


"""
percentage = promptPercentage()
print("Your bill is $", bill, sep="")
print("Your percentage is ", percentage, "%.", sep="")
percentage = rateServer()
print("Your new percentage is ", percentage, "%.", sep="")
tip = promptTipAmount()
print("Your manual tip entry is $", tip, sep="")
"""