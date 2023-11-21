def repeat(num):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat


@repeat(2)
def greet(name):
    print(f"Hello {name}")


greet("Lilly")
