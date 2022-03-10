"""
Name: Tennessee Tremain
Course: CS-175L
Program: Average From Input File
"""

def main():
    #Initialize Variables
    counter = 0
    add = 0
    #Open File
    avgFile = open("numbers.txt","r")
    #For Loop
    for num in avgFile:
        n = float(num)
        add+=n
        print(f"I read in {counter+1} number(s) Current number is: {n:7.2f} Total is {add:7.2f}")
        counter+=1
    avgFile.close()
    print(f"Average: {(add/counter):.1f}")
#Call Function
main()
