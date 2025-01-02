from operator import itemgetter, attrgetter;

class Student:
    def __init__(self, name, grade, age):
        self.name = name;
        self.grade = grade;
        self.age = age;
    
    def __repr__(self):
        return repr((self.name, self.grade, self.age));

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
];

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

# print( sorted(student_objects, key = lambda student : student.age) );

# print( sorted(student_tuples, key = itemgetter(2)) );
# print( sorted(student_objects, key = attrgetter('age')) );

## Multiple Levels of Sorting
# print( sorted(student_tuples, key = itemgetter(1, 2)) );
# print( sorted(student_objects, key = attrgetter('grade', 'age')) );

class Counter:
    def __init__(self, id):
        self.name = id;
        self.count = 0;

    def increment(self):
        self.count += 1;

    def tally(self):
        return self.count;

    def __str__(self):
        return f"The count is {self.count} for {self.name}.";

    def __repr__(self):
        return f"Counter ({self.name}, {self.count})";

if __name__ == "__main__":
    heads = Counter("heads");
    tails = Counter("tails");

    heads.increment();
    heads.increment();
    tails.increment();

    print(f"{repr(heads)} {repr(tails)}");
    print(heads.tally() + tails.tally());