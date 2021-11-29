def is_leap(year):
    """determines if a given year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:

        return False

def days_in_month(year,month):
    """outputs the number of days in a given month and year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if month > 12 or month < 1:
        return "invalid input"
    # if month is february in a leap year, the days are 29
    if is_leap(year) and month == 2:
        days = 29
        return days
    # for all other years and months return the days 
    # remember that the index begins at 0 therefor 'month - 1' returns the correct element
    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)