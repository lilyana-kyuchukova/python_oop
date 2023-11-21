def vowel_filter(function):
    def wrapper():
        vowels = ["a", "e", "i", "o", "u", "y"]
        result = [l for l in function() if l in vowels]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
