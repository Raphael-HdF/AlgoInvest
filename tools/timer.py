import time
from functools import wraps


def timer(function):
    @wraps(function)
    def wrapper_timer(*args, **kwargs):
        time_start = time.time()
        result = function(*args, **kwargs)
        time_end = time.time()
        duration_time = time_end - time_start
        print(f"Function '{function.__name__}' ran in {duration_time} seconds")
        return result

    return wrapper_timer
