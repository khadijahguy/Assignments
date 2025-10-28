# Creator : Khady Gueye

"""
THis program will take the users word and figure  out how many points it is worth.
"""

lettersdict = {
    "A" : 1, "B" : 3, "C" : 3, "D" : 2, "E" : 1, "F" : 4, "G" : 2, "H" : 4, "I" : 1,
    "J" : 8, "K" : 5, "L" : 1, "M" : 3, "N" : 1, "O" : 1, "P" : 3, "Q" : 10, "R" : 1, 
    "S" : 1, "T" : 1, "U" : 1, "V" : 4, "W" : 4, "X" : 8, "Y" : 4, "Z" : 10,
}

def calculate_points(word):
    """Calculate the total points of a given word based on Scrabble letter values."""
    total_points = 0
    for letter in word:
        if letter in lettersdict:
            total_points += lettersdict[letter]
    return total_points

def main():
    while True: 
        word = input(":> ")
        word = word.upper()

        if word in ["QUIT", "STOP", "Q"]:
            break

        points = calculate_points(word)
        print(f"{word} is worth {points} points.")

# Call the main function
if __name__ == "__main__":
    main()