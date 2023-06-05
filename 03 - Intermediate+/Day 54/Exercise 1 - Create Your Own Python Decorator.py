import time

def speed_calc_decorator(function):
    start_time = time.time()
    function()
    end_time = time.time()
    elapsed_time = end_time - start_time
    result = f"{function.__name__} run speed: {elapsed_time}s"
    print(result)

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i