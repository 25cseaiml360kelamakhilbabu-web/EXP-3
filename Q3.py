# Question 3: WAP to check the leap year.  
# Answer:Python
def check_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return False
    else:
        return False

year = int(input("enter the year"))
if check_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")