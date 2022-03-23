"""
Name: Tennessee Tremain
Course: CS-175L
Program: Average from input file with exception handling
"""

def main():
    #Open File
    try:
        numFile = open("numbers.txt","r")
    #If the file is not found
    except IOError:
        print("File not found!")
    #If the file is found
    else:
        #Call Functions, Print
        denominator, numerator = getNums(numFile)
        avg = average(numerator,denominator)
        print(f"The average of your {numerator} understandable numbers from the file is {avg}.")

#Function to get numbers
def getNums(file):
    #Initialize variables
    cont = True
    count = 0
    nums = 0
    read = file.readline()
    #Iterate through
    while cont:
        try:
            numRead = float(read)
        #Omit wrong data
        except ValueError:
            print("This is not a number! Continuing with rest of data...")
        #Include this data
        else:
            nums+=1
            print(f"Number {nums} included!")
            count+=numRead
        read = file.readline()
        #Break out of reading
        if read == "":
            cont = False
    return count, nums

#Average Function
def average(numOfNums,totalCount):
    return (totalCount/numOfNums)

#Run Program
if __name__ == "__main__":
    main()
