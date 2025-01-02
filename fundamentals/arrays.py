# iterable: an object capable of return its members one at a time
# list
# str
# tuple
# dict
# file objects
# user-defined objects of any class that contains __iter__() method or with a __getitem__()

# Sequence Types: list, tuple, range

## list
# in order: sort (return None) 
onions = [1.0 for _ in range(80)];
numbers = [1, 4, 2, 3, 0];
numbers.sort();

# sorted
sorted_numbers = sorted(numbers);
sorted_arr = sorted({ 1: "D", 2: "B", 3: "A", 4: "E", 5: "A" }); # dict is iterable, just take the keys in consideration
sorted_str = sorted("This is a test string from Andrew".split(), key = str.casefold); # casefold converts string to lowercase

## tuple (immutable sequences)
myTuple = ('john', 'A', 15);
student_tuples = [
    ('Linda', 'C', 10),
    ('Jesus', 'B', 12),
    ('Ariana', 'A', 15),
]
sorted_tuples = sorted(student_tuples, key = lambda student: student[0].casefold()) # sort by age

## range
list(range(10));                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11));             # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0, 30, 5));          # [0, 5, 10, 15, 20, 25]
list(range(0, 10, 3));          # [0, 3, 6, 9]
list(range(0, -10, -1));        # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(0));                 # []
list(range(1, 0));              # []
