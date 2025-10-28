# Creator: Khady Gueye

""" This is a program that implements the Age class. """

class Age:
    def __init__(self, years, months, days):
        self.years = years
        self.months = months
        self.days = days

    def __str__(self):
        return f"{self.years} years {self.months} months {self.days} days"

    def __add__(self, other):
        # Add years, months, and days
        total_days = self.days + other.days
        total_months = self.months + other.months + (total_days // 30)
        total_years = self.years + other.years + (total_months // 12)

        days = total_days % 30
        months = total_months % 12
        years = total_years

        return Age(years, months, days)

# Driver code
age1 = Age(2, 3, 22)
age2 = Age(3, 4, 2)
age3 = Age(10, 8, 10)

print(age1 + age2) 
print(age1 + age3)