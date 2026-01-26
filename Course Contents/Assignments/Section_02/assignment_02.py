import json

# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:

Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""

# your code below:

Person = {
    "Tom": {"Age": 22,
            "Salary": 20000,
            "Owns": ["jacket", "Car", "TV"]
            },
    "Mike": {"Age": 27,
             "Salary": 24000,
             "Owns": ["boat", "laptop", "bike"]
             }
}

# I should get extra points for formatting the dictionary nicely !

# Here's a method or two for printing the dictionary -

# indent=4 gives nice formatting, sort_keys=False keeps your original order
print("JSON format:")
print(json.dumps(Person, indent=4, sort_keys=False))
print("")

#Also full iteration with spanky formatting
for name, details in Person.items():
    print(f"Person: {name}")
    print(f"  Age    : {details['Age']}")
    print(f"  Salary : £{details['Salary']:,}")       # adds thousands separator and £
    print("  Owns   :")
    for item in details["Owns"]:
        print(f"    - {item}")
    print("-" * 20)  # optional separator line for clarity















# Solution

# my_list = [{'Tom': {'salary': 20000, 'age': 22, 'owns': ['jacket', 'car', 'TV']}},
#            {'Mike': {'salary': 24000, 'age': 27, 'owns': ['bike', 'laptop', 'boat']}}]
