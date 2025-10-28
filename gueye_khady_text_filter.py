# Creator: Khady Gueye

"""
This program remove banned words from the users input.
"""

def filter_text(message):
    # Define a list of banned words
    banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]
    
    # Split the input message into words
    words = message.split()
    
    # Create a list to hold the filtered words
    filtered_words = []

    # Loop through each word in the original message and add to the list
    for word in words:
        if word not in banned_words:
            filtered_words.append(word)
    
    filtered_text = ""
    for word in filtered_words:
        filtered_text += word + " "  # Add a space after each word

    return filtered_text

if __name__ == "__main__":
    # Ask the user for input
    message = input("Input Message: ")
    
    filtered_message = filter_text(message)
    
    # Print out the filtered message
    print(f'Output Message: {filtered_message}')
