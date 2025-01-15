import random;

# Generate random array
def generate_array(size, lower_bound=-100, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)];