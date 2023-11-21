from functools import wraps


def uppercase(func):
    @wraps(func)
    def wrapper():
        upper = func().upper()
        return upper
    return wrapper


@uppercase
def say_hi():
    """saying hi"""
    return "hello there"


print(say_hi())

print(say_hi.__name__)
print(say_hi.__doc__)
