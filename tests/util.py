import time


def time_function(func, *args, **kwargs):
    start_time = time.perf_counter_ns()
    result = func(*args, **kwargs)
    end_time = time.perf_counter_ns()

    elapsed_time = end_time - start_time
    print(f"{func.__name__} - {elapsed_time} ns")
    return result
