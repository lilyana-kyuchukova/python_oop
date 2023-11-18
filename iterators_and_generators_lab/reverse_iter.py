class reverse_iter:
    def __init__(self, some_iter):
        self.some_iter = some_iter
        self.ind = len(self.some_iter)

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind == 0:
            raise StopIteration
        self.ind -= 1
        return self.some_iter[self.ind]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
