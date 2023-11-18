class vowels:
    def __init__(self, some_string):
        self.some_string = [l for l in some_string if l.lower() in ('a', 'e', 'i', 'o', 'u', "y")]
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.x == len(self.some_string):
            raise StopIteration

        x = self.x
        self.x += 1
        return self.some_string[x]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)