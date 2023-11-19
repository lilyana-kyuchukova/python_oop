class countdown_iterator:
    def __init__(self, count):
        # self.count = count
        # self.iterable = [x for x in range(0, self.count + 1)]
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        # if len(self.iterable) == 0:
        if self.count <= 0:
            raise StopIteration

        self.count -= 1

        return self.count  # self.iterable.pop()


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")


