"""An extra day is added to the calendar almost every four years as February 29. and the day is called a leap day. lt
corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains
a leap day.
In the Gregorian calendar. three conditions are used to identify leap years:
The year can be evenly divided by 4. is a leap year. unless:
o The year can be evenly divided by 100. it is NOT a leap year. unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar. the years 2000 and 2400 are leap years. while 1800. 1900. 2100. 2200.
2300 and 2500 are NOT leap years. Source
Task
Civen a year. determine whether it is a leap year- If it is a leap year. return the Boolean T rue. otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the i s _ leap function. lt is only
necessary to complete the i s_leap function.
Input Format
Read year. the year to test.
Constraints
1900 year 105
Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
Sample Input O
1990
Sample Output O
False"""

def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap=True
        else:
            leap=True 
    return leap

year = int(input())