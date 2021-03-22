# multiplication
result = 3 * 5
print(result)

# power operation
result = 3 ** 5
print(result)

# list
zeros = [0] * 10
onetwos = [0, 1] * 5
print(zeros)
print(onetwos)

# tuple
zeros = (0,) * 10
onetwos = (0, 1) * 5
print(zeros)
print(onetwos)

# string
A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)

# *args, **kwargs ang keyword-only arguments
def my_func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

my_func("Hey", 3, [0, 1, 2], name="Alex", age=8)

# Parameters after '*' or '*identifier' are keyword-only parameters and may only be passed using keyword arguments.
def num(a, b, *, c):
    print(a, b, c)

num(1, 2, c=3)

# unpacking for function arguments
def var(a, b, c):
    print(a, b, c)

# length must match
my_list = [1, 2, 3]
var(*my_list)

my_string = "ABC"
var(*my_string)

# length and keys must match
my_dict = {'a': 4, 'b': 5, 'c': 6}
var(**my_dict)

# unpacking containers
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

*beginning, last = numbers
print(beginning)
print(last)

first, *end = numbers
print(first)
print(end)

first, *middle, last = numbers
print(first)
print(middle)
print(last)

first, *middle, secondlast, last = numbers
print(first)
print(middle)
print(secondlast)
print(last)

# Merge iterables into a list
my_tuple = (1, 2, 3)
my_list1 = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list1, *my_set]
print(new_list)

# Merge dictionaries
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

new_dict = {**dict_a, **dict_b}
print(new_dict)