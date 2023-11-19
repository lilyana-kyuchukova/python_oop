class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iteration = -1

        # self.iterable = [x * self.step for x in range(0, self.count)]
        # self.x = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.iteration == self.count - 1:
        # if self.x == len(self.iterable):
            raise StopIteration

        self.iteration += 1

        # x = self.x
        # self.x += 1
        # return self.iterable[x]
        return self.iteration * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


