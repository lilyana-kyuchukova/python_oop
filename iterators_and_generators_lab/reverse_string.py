def reverse_text(text):
    # for l in range(len(text) -1, -1, -1):
    #     letter = text[l]
    #     yield letter

    for l in reversed(text):
        yield l


for char in reverse_text("step"):
    print(char, end='')