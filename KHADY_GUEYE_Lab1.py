# Creator : Khady Gueye
"""This a program that detects if a inputted year is a leap year."""

def is_leap_year(year):
    # Check for leap year
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

# Take input from the user
year = int(input())

# Output
if is_leap_year(year):
    print(f"{year} - leap year")
else:
    print(f"{year} - not a leap year")
