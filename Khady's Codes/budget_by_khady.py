# Creator : Khady Gueye

"""
This a simple budget calculator I'm creating for annyone to use to start creating a plan.
"""

# Ask the user for their monthly salary so the program can create a plan ideal for them. (For now they have to calulate monthly, room for future improvements.)
monthly = int(input('Please enter your monthly salary: $'))

# Calculations
weekly = monthly // 4
#print(f'Your weekly salary is {weekly}')  (to check calculations)
needs = (50/100)* monthly
wants = (30/100)* monthly
saving = (20/100)* monthly

# Print their 50/30/20 budget so they can determine how they want to distrubte it amongst the cateogries.
print(' ')
print('Great! This budgeting software uses 50/30/20 rule of thumb to get you started.')
print("Let's see how you're money is distrubuted: ")
print(' ')
print(f'You currently have ${needs} to spend on needs each month.')
print(f'You currently have ${wants} to spend on needs each month.')
print(f'You currently have ${saving} to spend on needs each month.')
print(' ')
input('Would you like to go more in depth?')





# Housing 
# housing = int(input('Please enter the amount you spend on housing each month: '))
# Calculate
# other_needs = needs - housing 
# print(' ')
# print(f'Great! You have ${other_needs} leftover.')



# housing = input('How much to you spend on housing each month (including utilities, morgage etc.., if none, put 0): ')





