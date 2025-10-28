# Creator: Khady Gueye

"""
This program takes your sentences and put's it in reverse.
"""

# Ask the person for a sentence

sentence = input("Please Enter Your String: ")
new_sentence = " "


# While loop for reversing the sentence
while sentence != "q" and sentence != "quit" and sentence != "Quit":
    for i in range ( len(sentence)-1,-1,-1 ):
        new_sentence += sentence [i]
    print (f'Reversed:{new_sentence}')
    print(' ')
    sentence = input ("Please Enter Your String: ")