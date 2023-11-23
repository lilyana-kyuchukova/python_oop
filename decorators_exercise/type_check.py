def type_check(type_data):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_data):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(list)
def first_letter(word):
    return word[0]
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))