class sequence_repeat:
    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.inx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.inx == self.num - 1:
            raise StopIteration

        self.inx += 1

        return self.text[self.inx % len(self.text)]


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

