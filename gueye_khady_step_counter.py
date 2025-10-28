# Creator : Khady Gueye

""" This is  program that takes number of steps and turns it into its mile form."""

# Create a class for the Type of Value error.
class NegativeValueError(Exception):
    pass

def steps_to_miles(steps):
    # Check if number is a valid number
    try:
        steps = int(steps)
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered.")
    
    # Check for negative step count
    if steps < 0:
        raise NegativeValueError("Exception: Negative Step Count Entered.")
    
    # Convert the steps to miles
    miles = steps / 2000
    return miles

def main():

    user_input = input("Enter the # of steps:> ")
    
    try:
        # Calculate miles
        miles = steps_to_miles(user_input)
        print(f"{miles:.2f} miles")
    
    except ValueError as VE:
        # Print the ValueError
        print(VE)
    
    except NegativeValueError as NVE:
        # Print the NegativeValueError
        print(NVE)

if __name__ == "__main__":
    main()
