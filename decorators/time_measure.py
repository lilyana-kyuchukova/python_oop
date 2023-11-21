from time import sleep, time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"Execution time of {func.__name__}: {end - start}")
        return result
    return wrapper


@measure_time
def slow_func(n):
    sleep(n)


slow_func(2)