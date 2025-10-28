# Creator: Khady Gueye

"""
This is a calendar that tells you what quarter we are in at Northwestern.
"""

# Get users input the month and day it current is in.
month = (input('Please enter the month: '))
day = int(input('Please enter the day: '))

# List of valid quotes
my_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# Check if month input is in the list
if month not in my_list:
    print ("Month is not valid. Please try again!")
else:
# Check which is correct
    if month in ["October", "November"]:
        semester = "Northwestern's Fall quarter."
    elif month == "February":
        semester = "Northwestern's Winter quarter."
    elif month in ["May", "April"]:
        semester = "Northwestern's Spring quarter."
    elif month in ["July", "August"]:
        semester = "Northwestern's Summer quarter."
    elif month == "September" and day >= 24:
        semester = "Northwestern's Fall quarter."
    elif month == "December" and day <= 14:
        semester = "Northwestern's Fall quarter."
    elif month == "January" and day >= 6:
        semester = "Northwestern's Winter quarter."
    elif month == "March" and day <= 22:
        semester = "Northwestern's Winter quarter."
    elif month == "June" and day <= 13:
        semester = "Northwestern's Spring quarter."
    elif month == "June" and day >= 23:
        semester = "Northwestern's Summer quarter."
    else:
        semester = "is a academic break."


# Print the statement.
print(f"{month} {day} is during {semester}")
