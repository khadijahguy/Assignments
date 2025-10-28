# Creator: Khady Gueye

# Task 1: Handling Built-in Exceptions

def handle_exceptions():
    try:
        # TypeError Example
        print("5" + 5) 
    except TypeError:
        print("TypeError: Cannot add string and integer.")
    
    try:
        # ValueError Example
        num = int("abc")  
    except ValueError:
        print("ValueError: Cannot convert string to integer.")
    
    try:
        # KeyError Example
        my_dict = {"name": "Alice"}
        print(my_dict["age"]) 
    except KeyError:
        print("KeyError: Key doesn't exist in dictionary.")
    
    try:
        # AttributeError Example
        num = 5
        num.append(10) 
    except AttributeError:
        print("AttributeError: 'int' object has no attribute 'append'.")
    
    try:
        # RecursionError Example
        def recursive():
            return recursive()
        recursive()
    except RecursionError:
        print("RecursionError: Maximum recursion exceeded.")

handle_exceptions()

# Task 2: Custom Exception Handling
class EmailFormatError(Exception):
    pass

def is_valid_email(email: str):
    if email.count('@') == 1 and email.endswith("@student.gsu.edu") and email[0].isalpha():
        return True
    else:
        raise EmailFormatError("Please enter a valid email address.")
    
try:
    print(is_valid_email("test@student.gsu.edu"))  # Should return True
    print(is_valid_email("1test@student.gsu.edu"))  # Should raise EmailFormatError
except EmailFormatError as e:
    print(e)