#  Problem 6. Leap Years and Days in a Month

"""
A year is a leap year if it is divisible by 4, except century years (divisible by 100),
 which are leap years only if they are also divisible by 400. 
(a) Write is_leap(year) that returns True or False using one boolean expression with and / or. 
(b) Write days_in_month(month, year) that returns 28, 29, 30 or 31, 
or None if the month is not between 1 and 12. Use in to test the 30-day months (4, 6, 9, 11). 
(c) Print whether 1900, 2000, 2024 and 2026 are leap years. 
(d) Count the leap years from 2000 to 2100 (both included) with a loop. 

"""

# (a) leap year with ONE boolean expression
def is_leap(year):
    return (year % 4 == 0 and year % 100 !=0) or year % 400 == 0

# (b) days in a month
def days_in_month(month, year):
    if month < 1 or month > 12:
        return None
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

# (c) print wether each year is leap
for year in [1900, 2000, 2024, 2026]:
    if is_leap(year):
        print(year, "leap")
    else:
        print(year, "not leap")

# Days in month tests
print("Feb 2024:", days_in_month(2, 2024),
      "| Feb 2026:", days_in_month(2, 2026),
      "| Apr:", days_in_month(4, 2026),
      "| month 13:", days_in_month(13, 2026))

# (d) count leap years from 2000 to 2100 (both included)
count = 0
for year in range (2000, 2101):
    if is_leap(year):
        count = count + 1
print("Leap years from 2000 to 2100:", count)
        
    
