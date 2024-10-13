def calculate_ticket(speed_limit, driving_speed):
    speed_difference = driving_speed - speed_limit

    if speed_difference <= -10:
        return 50  # Driving 10 mph under or slower
    elif 0 < speed_difference <= 20:
        return 75  # Driving 6 - 20 mph over
    elif 20 < speed_difference <= 40:
        return 150  # Driving 21 - 40 mph over
    elif speed_difference > 40:
        return 300  # Driving faster than 40 mph over
    else:
        return 0  # No ticket


# Taking input from the user
speed_limit = int(input("Please enter the speed limit for the road: "))
driving_speed = int(input("Please enter the vehicle's recorded speed: "))

# Calculate ticket amount     
ticket_amount = calculate_ticket(speed_limit, driving_speed)

if ticket_amount == 0:
    print("There is no fine.")
else:
    print(f"The speeding fine is ${ticket_amount}")