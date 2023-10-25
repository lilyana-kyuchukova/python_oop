
def choice_pattern():
    pattern = input("Pick a pattern ->\n- Triangle\n- Rhombus\n- Square\nPattern choice: ")
    size = int(input("Enter pattern size: "))

    return pattern, size


def print_pattern_data(space_data, pattern_char):
    print(" " * space_data + "* " * pattern_char)


def rhombus_pattern(*data):
    pattern, size = data

    if pattern == "Rhombus":
        for x in range(size):
            space = size - x - 1
            char = x + 1
            print_pattern_data(space, char)

        for x in range(size - 2, -1, -1):
            space = size - x - 1
            char = x + 1
            print_pattern_data(space, char)

    elif pattern == "Triangle":
        for x in range(size):
            space = size - x - 1
            char = x + 1
            print_pattern_data(0, char)

    elif pattern == "Square":
        for x in range(size):
            print_pattern_data(0, size)


rhombus_pattern(*choice_pattern())

