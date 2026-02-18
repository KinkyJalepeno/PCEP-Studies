
"""
    In Python, *args and **kwargs are special syntax that let your functions accept a variable number of arguments.


    *args (the * is what matters — "args" is just a common name) allows a function to receive any number of
    positional arguments as a tuple.

"""

# *args example
print("*args example")
def add_numbers(*args):
    return sum(args)

print(add_numbers(5, 10))          # SUM 15
print(add_numbers(1, 2, 3, 4))     # SUM 10
print(add_numbers(7))              # SUM 7
print(add_numbers())               # SUM 0

# OUTPUT:
# 15
# 10
# 7
# 0



"""
    **kwargs (double asterisk) does the same thing as *args, but for keyword arguments (named arguments). 
    It collects them and puts key value pairs into a dictionary:
"""
# **kwargs example
print("", end="\n\n")
print("**kwargs example")
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Anna", age=28, city="Oslo", hobby="climbing")
print("", end="\n\n")

# Output:
# name: Anna
# age: 28
# city: Oslo
# hobby: climbing

"""
    You can also combine normal parameters, *args and **kwargs — but they must appear in this exact order:
"""

# combo example
print("Combination example")
def example(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

example(10, 20, 30, 40, 50, name="Sara", active=True)

# get a value from a key
print("", end="\n\n")
def my_function(**kwargs):
    print(kwargs.get("name"))

my_function(name="Dave", age=26, weight=200, active=True)
my_function(name="Bev", age=56, weight=400, active=True)
# if you try to get a value from a key that does not exist, "None" will be returned

