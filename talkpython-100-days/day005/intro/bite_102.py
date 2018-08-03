VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        user_input = str.lower(input("Enter color: ").strip())
        if user_input == 'quit':
            print('bye')
            break
        if user_input not in VALID_COLORS:
            print("Not a valid color")
            continue
        print(user_input)
