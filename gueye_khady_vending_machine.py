# Creator : Khady Gueye

"""
This program is a vending machine. So grateful for only one lab, nearly cried!
"""

# Create a class for the vending machine.
class VendingMachine:
    def __init__(self, soda, water, coffee):
        self.soda = soda
        self.water = water
        self.coffee = coffee

    # Define a function for purchasing from the vending machine.
    def buy(self, drink):
        if drink == "Soda":
            if self.soda > 0:
                self.soda -= 1
            else:
                print("Sorry, we don't have anymore soda. :( ")
        elif drink == "Water":
            if self.water > 0:
                self.water -= 1
            else:
                print("Sorry, we don't have anymore water. :( ")
        elif drink == "Coffee":
            if self.coffee > 0:
                self.coffee -= 1
            else:
                print("Sorry, we don't have anymore coffee. :( ")
        else:
            print("We don't have that! Sorry!")

    # Define a function for restocking the vending machine.
    def restock(self, drink, quantity):
        if drink == "Soda":
            self.soda += quantity
        elif drink == "Water":
            self.water += quantity
        elif drink == "Coffee":
            self.coffee += quantity
        else:
            print("We don't have that! Sorry!")

    # Define a function for inventory in the vending machine.
    def inventory(self):
        print(" ")
        print(f"Inventory \nSoda: {self.soda} bottles \nWater: {self.water} bottles \nCoffee: {self.coffee} bottle")
        print(" ")

# Define a main function. 
def main():

    # Assign the variable for vending machine.
    vending_machine = VendingMachine(soda=10, water=10, coffee=10)

    print("Hi! How may we serve you today? :)")

    while True:
        # Take a command from the user.
        command = input(":> ").strip().capitalize()

        # Check for stop the code.
        if command in ['Quit', 'Q']:
            break

        # Run the Restock command.
        elif command == "Restock":
            print(" ")
            print("Please select an option: ")
            print(f"1 - Soda \n2 - Water \n3 - Coffee")
            print(" ")
            choice = input(":> ").strip()
            if choice == "1":
                drink = "Soda"
            elif choice == "2":
                drink = "Water"
            elif choice == "3":
                drink = "Coffee"
            else:
                print("Not one of the choices!")
                continue

            # Enter amount and add it to the vending machine by calliing the function.
            print(" ")
            print("Please enter an amount:")
            quantity = int(input(":> "))
            if quantity > 0:
                vending_machine.restock(drink, quantity)
        
        # Run the Restock command.
        elif command == "Buy":
            print(" ")
            print("Please select an option: ")
            print(f"1 - Soda \n2 - Water \n3 - Coffee")
            print(" ")
            choice = input(":> ").strip()

            if choice == "1":
                drink = "Soda"
            elif choice == "2":
                drink = "Water"
            elif choice == "3":
                drink = "Coffee"
            else:
                print("Not one of the choices!")
                continue

            # Buy from vending machine by calliing the function.
            vending_machine.buy(drink)

        # Call the Inventory command to see what's currently available. 
        elif command == "Inventory":
            vending_machine.inventory()

        # Otherwise, let the user know the we can't understand the caommand given.
        else :
            print("We can not help you today!")
            continue         

# Call the main function 
if __name__ == "__main__":
    main()