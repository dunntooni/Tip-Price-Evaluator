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
#Prompts the user for the cost of their bill
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

#Prompts the user for a percentage to use for calculating a tip
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

#A dictionary designed to convert a rating into a percent
def ratingToPercent(rating):
   percentDic = {
      1: 5,
      2: 10,
      3: 15,
      4: 25,
      5: 35
   }
   return percentDic.get(rating, "Invalid")

#Prompts the user for a rating, and asks the user if the associated percent is satisfactory
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

#Prompts the user for a manual tip entry
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

#Uses the bill to generate a tip based on the desired percent
def percentToTip(percent, bill):
   return float(bill) * (float(percent) / 100)

# The main driver function. Uses a loop to prompt the user for
# the means of calculating their tip/bill. Returns a tip value.
def getTip(bill):
   tip = 0.00
   userInput = None
   inputInvalid = True
   while inputInvalid == True:
      print("------------------------------------------------------------------")
      print("How would you like to calculate your tip?")
      print("Type 'p' to input a percentage.")
      print("Type 'q' to calculate a price based on the quality of your server.")
      print("Type 'm' to manually input a tip amount.")
      print("------------------------------------------------------------------")
      userInput = input(">")
      if userInput == "p" or userInput == "q" or userInput == "m":
         inputInvalid = False
   if userInput == "p":
      tip = percentToTip(promptPercentage(), bill)
   elif userInput == "q":
      tip = percentToTip(rateServer(), bill)
   elif userInput == "m":
      tip = promptTipAmount()
   return tip

# Adds the tip and bill values
def calculateTotal(bill, tip):
   total = 0.00
   total = float(bill) + float(tip)
   return total

# Displays the finished result
def displayTotal(total):
   total = "{:.2f}".format(total)
   print("Your total is $", total, ".", sep="")

bill = promptBillAmount()
tip = getTip(bill)
total = calculateTotal(bill, tip)

displayTotal(total)


"""
Testing code:
percentage = promptPercentage()
print("Your bill is $", bill, sep="")
print("Your percentage is ", percentage, "%.", sep="")
percentage = rateServer()
print("Your new percentage is ", percentage, "%.", sep="")
tip = promptTipAmount()
print("Your manual tip entry is $", tip, sep="")
"""