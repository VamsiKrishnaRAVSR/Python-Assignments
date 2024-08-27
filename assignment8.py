import time
import psutil
def measure_time_and_memory(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process()
        memory_before = process.memory_info().rss
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        memory_after = process.memory_info().rss
        memory_used = memory_after - memory_before
        print(f"Function {func.__name__} took {elapsed_time:.5f} seconds to execute and consumed {memory_used:.5f} of memory.")
        return result
    return wrapper

@measure_time_and_memory
def my_function():
    a = [i for i in range(10000000)]
    print(a.__len__)
    time.sleep(2)

my_function()
