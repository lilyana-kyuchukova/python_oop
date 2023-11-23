def cache(func):


    def wrapper(args):
        if args not in wrapper.log:
            wrapper.log[args] = func(args)
        return wrapper.log[args]

    wrapper.log = dict()
    return wrapper



@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)