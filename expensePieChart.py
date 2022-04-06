"""
Name: Tennessee Tremain
Course: CS-175L
Program: Expense Pie Chart
"""
import matplotlib.pyplot as plt
import numpy as np

def fileLists():
    fullList = []
    titles = []
    prices = []
    try:
        file = open("expenses.txt","r")
    except IOError:
        print("File not found!")
    else:
        for line in file:
            line = line.strip("\n")
            fullList.append(line.split("\t"))
        for nl in fullList:
            titles.append(nl[0])
            prices.append(nl[1])
        file.close()
    return titles,prices
def main():
    t,p = fileLists()
    #n = np.array(p)
    plt.pie(p,labels = t)
    plt.show()

if __name__ == "__main__":
    main()
        
