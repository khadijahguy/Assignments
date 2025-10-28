# Creator : Khady Gueye

"""
This program that takes in text as input and converts it into a bag of words.
"""

def build_dictionary(words_list):
    words_dict = {}
    for word in words_list:
        word = word.lower() 
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict

def main():
    text = input(":> ")
    words = text.split()
    word_dict = build_dictionary(words)
    sorted_word_dict = sorted(word_dict.items(), key=lambda item: item[1])

    print("Words List: \n", words)
    
    print("Bag of Words: \n", sorted_word_dict)

if __name__ == "__main__":
    main()
