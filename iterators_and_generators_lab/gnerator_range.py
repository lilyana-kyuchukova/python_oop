def genrange(s, e):
    for i in range(s, e + 1):
        yield i


print(list(genrange(1, 10)))