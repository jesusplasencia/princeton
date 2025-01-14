import random;
import time;

# Generate random array
def generate_array(size, lower_bound=-100, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)];

# Timing wrapper
def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time