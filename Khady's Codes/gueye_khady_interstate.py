#This is Khady Gueye's Interstate Code

interstate_number = int(input("Please enter the interstate number:"))
service = interstate_number % 100

if service == 0:
    print(f'{interstate_number} is not valid highway interstate number.')
    exit()
elif interstate_number >= 100 and interstate_number <= 999:
    print(f'I-{interstate_number} is auxilliary, serving I-{service},', end='')
else:
    print(f'I-{interstate_number} is primary, ', end='')

#Determines direction
if interstate_number % 2 == 0:
    print('going east/west.')
else:
    print('going north/south.')