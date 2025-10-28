# Creator: Khady Gueye

"""
Translate feet into how many steps were taken.
"""

# Ask user for how many feet they walked
feet = float(input("Please enter distance travelled in feet: "))

# Define the function
def feet_to_steps(feet):
    feet_to_steps = feet // 2.5
    return feet_to_steps

#Call function forward and set it equal to steps (Just for a shorter name to call)
steps = feet_to_steps(feet)

# Print the users steps
print(f'{steps} steps')