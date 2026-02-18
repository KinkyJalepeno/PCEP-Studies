# whatever value you send to a function as an argument will override anything asigned in the function header

def greet_person(name='Dave'):
    print('Hello, ' + name + '!')

greet_person('The Bev') # output Hello, The Bev!

# because we have assigned a value to name in the header we can get away with not sending an argument when
# calling the function.

greet_person() # output will default to Hello, Dave!



# adding function documentation

def greet_person(name='Dave'):
    """
    DOCSTRING: this prints a greeting
    INPUT: requires a string and has default value of 'Dave'
    """

    print('Hello, ' + name + '!')
    print('Just some bumf')
    print('1 + 1 = 2')

greet_person()


# return a value from function
def get_remainder(value1, value2) -> int:
    return value1 % value2

print(get_remainder(50, 7))



