"""
Name: Tennessee Tremain
Program: Stocks
"""
#Receive Inputs
commRate = float(input("What was the comission rate? " ))
shares = int(input("How many shares did you purchase? "))
purchase = float(input("What was the purchase price? "))
selling = float(input("What was the selling price? "))
#Calculations
amount = purchase*shares
commPaidPre = amount*commRate
sold = selling*shares
commPaidPost = sold*commRate
totalComm = commPaidPre + commPaidPost
profit = sold-amount-totalComm
#Print Statements with formatting
print(f"Amount paid for stock: ${amount:.2f}")
print(f"Commission paid on the purchase: ${commPaidPre:.2f}")
print(f"Amount the stock sold for: ${sold:.2f}")
print(f"Commission paid on the sale: ${commPaidPost:.2f}")
print(f"Total commission paid: ${totalComm:.2f}")
print(f"Profit (positive or negative): ${profit:.2f}")
