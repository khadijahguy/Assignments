# Define the lists for different character types
vowels = ['a', 'e', 'i', 'o', 'u']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = [',', ';', '.', '?', '!']

# User has to enter a character
user_input = input("Enter a character:").strip()

# Check if the input is a single character
if len(user_input) != 1:
    print("Please enter a single character.")
else:
    char = user_input.lower()
    
    # Determine the type of character
    if char in vowels:
        print(f"The character '{user_input}' is a vowel.")
    elif char in digits:
        print(f"The character '{user_input}' is a digit.")
    elif char in punctuation:
        print(f"The character '{user_input}' is punctuation.")
    elif char.isalpha():  # Check if it is an alphabetic character (if not a vowel, then it is a consonant)
        print(f"The character '{user_input}' is a consonant.")
    else:
        print(f"The character '{user_input}' is neither a vowel, consonant, digit, nor punctuation.")