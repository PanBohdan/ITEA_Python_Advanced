import time


def decorator(num_of_repeats):
    print(num_of_repeats)
    start_timer = time.time()

    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_of_repeats):
                result = func(*args, **kwargs)
            return result, func.__name__
        return wrapper
    elapsed_timer = f"time taken by our program is {time.time() - start_timer}"
    print(elapsed_timer)
    return actual_decorator


@decorator(1000)
def multiplication(arg1, arg2):
    return arg1 * arg2


print(multiplication(1, 2))
