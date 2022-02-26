"""
Name: Tennessee Tremain
Course: CS-175L
Program: Functions Average and Grade Assignment
"""
#Takes in a score argument and returns letter grade
def determineGrade(score):
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 70):
        return "C"
    elif (score >= 60):
        return "D"
    else:
        return "F"

#Takes in 5 arguments (scores)
def calcAverage(s1,s2,s3,s4,s5):
    return ((s1+s2+s3+s4+s5)/5)

#Returns True/False to continue program
def repeat():
    r = input("Enter \'yes\' if you would like to do another calculation: ")
    if (r == "yes"):
        return True
    else:
        return False

#Make sure grade is in range
def valGrade(scoreNum):
    sVar = float(input("Enter score " + str(scoreNum) + ": "))
    while (sVar < 0) or (sVar > 100):
        print("Outside of range!  Try again!")
        sVar = float(input("Enter score " + str(scoreNum) + ": "))
    return sVar
    
#Main program...print statements/using functions
def main():
    r = True
    while r:
        t1 = valGrade(1)
        t2 = valGrade(2)
        t3 = valGrade(3)
        t4 = valGrade(4)
        t5 = valGrade(5)
        l1 = determineGrade(t1)
        l2 = determineGrade(t2)
        l3 = determineGrade(t3)
        l4 = determineGrade(t4)
        l5 = determineGrade(t5)
        average = calcAverage(t1,t2,t3,t4,t5)
        la = determineGrade(average)
        print("Score          Numeric Grade     Letter Grade")
        print("--------------------------------------------------")
        print(f"Score 1:{t1:>15.1f}{l1:>17}")
        print(f"Score 2:{t2:>15.1f}{l2:>17}")
        print(f"Score 3:{t3:>15.1f}{l3:>17}")
        print(f"Score 4:{t4:>15.1f}{l4:>17}")
        print(f"Score 5:{t5:>15.1f}{l5:>17}")
        print(f"Average:{average:>15.1f}{la:>17}")
        r = repeat()

#Run main program
main()
