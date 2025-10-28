# Creator : Khady Gueye

""" This program simulates a web browser's navigation using two stacks to manage back and forward page history based on user commands."""


def browser_simulator():
    back_stack = []                             # Stack for BACK history
    forward_stack = []                          # Stack for FORWARD history
    current_page = "http://www.google.com/"     # Start at homepage

    while True:
        try:
            command = input().strip()           # Read user command
        except EOFError:
            break

        if not command:
            continue

        parts = command.strip().split(maxsplit=1)
        action = parts[0]

        if action == "QUIT":
            break

        elif action == "VISIT":
            if len(parts) != 2:
                print("Ignored")
                continue
            url = parts[1]
            back_stack.append(current_page)     # Save current before visiting new
            current_page = url
            forward_stack.clear()               # Clear forward history
            print(current_page)

        elif action == "BACK":
            if not back_stack:
                print("Ignored")
            else:
                forward_stack.append(current_page)  # Save current to forward
                current_page = back_stack.pop()     # Go back
                print(current_page)

        elif action == "FORWARD":
            if not forward_stack:
                print("Ignored")
            else:
                back_stack.append(current_page)     # Save current to back
                current_page = forward_stack.pop()  # Go forward
                print(current_page)

        else:
            print("Ignored")                        # Invalid command

# Driver Code
if __name__ == "__main__":
    browser_simulator()
