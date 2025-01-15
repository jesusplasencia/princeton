from .divide_n_conquer import max_subarray_problem_brute_force, find_maximum_subarray
from helpers import generate_array, time_function

def test_algorithms():
    sizes = [10, 100, 1000, 5000, 10000];
    results = [];

    for size in sizes:
        test_array = generate_array(size);

        _, brute_time = time_function(max_subarray_problem_brute_force, test_array);
        _, optimized_time = time_function(find_maximum_subarray, test_array, 0, len(test_array) - 1);

        results.append((size, brute_time, optimized_time))
    
    print(f"{'Size':<10}{'Brute-Force Time':<20}{'Optimized Time':<20}")
    for size, brute_time, optimized_time in results:
        print(f"{size:<10}{brute_time:<20.6f}{optimized_time:<20.6f}")

# Run tests
test_algorithms()