# Creator: Khady Gueye

"""
This program allows the user to input R, G, B color values and gives the Hex value.
"""

# A function to reformat the value
def RGB_to_Hex(r, g, b):
    def to_hex(value):
        return format(value, '02X') 
# Define and excute hex code, so you can call it later
    hex_code = f"#{to_hex(r)}{to_hex(g)}{to_hex(b)}"
    return hex_code

# Calls a main function to take the input and make sure it is a interger
def main():
    print("RGB to Hex Converter")
    while True: # Create a Infinite Loop
        red_input = input("Enter Red Color Value: ")
        # Check for key word to stop program
        if red_input.lower() in ['quit', 'q', 'stop']:
            break
        
        green_input = input("Enter Green Color Value: ")
        blue_input = input("Enter Blue Color Value: ")
        
        # Check for Invalid input
        try:
            r = int(red_input)
            g = int(green_input)
            b = int(blue_input)
        except ValueError:
            print("Invalid")
            continue
    
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Invalid")
            continue

        # Define variable to function so you can call it to print
        hex_code = RGB_to_Hex(r, g, b)
        print(f"Hex Value: {hex_code}")

# Call the main function
if __name__ == "__main__":
    main()