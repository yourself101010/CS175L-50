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
print(f"Amount paid for stock: ${amount:.1f}")
print(f"Commission paid on the purchase: ${commPaidPre:.1f}")
print(f"Amount the stock sold for: ${sold:.1f}")
print(f"Commission paid on the sale: ${commPaidPost:.1f}")
print(f"Total commission paid: ${totalComm:.1f}")
print(f"Profit (positive or negative): ${profit:.1f}")
