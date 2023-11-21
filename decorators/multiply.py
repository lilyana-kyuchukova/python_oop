def multiply(times):
    # return lambda f: lambda *args, **kwargs: times * f(*args, **kwargs)
    def decorator(function):
        def wrapper(*args, **kwargs):  # we do not know what we are going to receive hence arg/kwargs
            return times * function(*args, **kwargs)

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))