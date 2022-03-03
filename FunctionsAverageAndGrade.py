"""
Name: Tennessee Tremain
Course: CS-175L
Program: Functions Average and Grade Assignment with Random
"""
#Import random
import myRandom


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
def getGrade():
    return myRandom.gen(1,100)
    
#Main program...print statements/using functions
def main():
    r = True
    add = 0
    while r:
        scores = []
        print("Score          Numeric Grade     Letter Grade")
        print("--------------------------------------------------")
        for i in range(1,6,1):
            t = getGrade()
            l = determineGrade(t)
            add+=t
            scores.append(t)
            print(f"Score {i}:{t:>15.1f}{l:>17}")
        average = calcAverage(scores[0],scores[1],scores[2],scores[3],scores[4])
        la = determineGrade(average)
        print(f"Average:{average:>15.1f}{la:>17}")
        r = repeat()

#Run main program
main()
