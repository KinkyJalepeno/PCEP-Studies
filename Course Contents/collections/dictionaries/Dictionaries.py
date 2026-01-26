dictionary = {"Name": "Dave",
              "Age": 56,
              "Sex": "Male"
              }

print(dictionary["Age"])

# iterate through dictionary key value pairs
for key, value in dictionary.items():
    print(key, value)

# Rules - Dictionaries cannot be sorted in any way
# pop will return a value and will still remove key/value from the dict
# dicts can have lists in them

# change a value - age set to 40
dictionary["Age"] = 46
print(dictionary["Age"]) # output 46

# add a key value pair
dictionary["Height"] = 172
for key, value in dictionary.items():
    print(key, value)

# add a list to dict
dictionary["Pockets"] = ["keys", "lighter"]

# print the list
print(dictionary["Pockets"])

# print the value for index 1 within the pockets list
print(f'The value at index 1 of the list within pockets is: {dictionary["Pockets"][1]}')

dictionary = {"Name": "Dave",
              "Age": 56,
              "Sex": "Male",
              "items": ["Orange",
                        {"k1": "some random value"}]
              }
# access the value for k1 which is at index 1 in the list contained in items
print(f'The value of k1 is: {dictionary["items"][1]["k1"]}')  # Output "Some random value"


# nested dictionary

person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland",
        "zipcode": "12345",
        "coordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    },
    "hobbies": ["reading", "hiking", "coding"]
}

# access deeply nested values -
print(person["address"]["coordinates"]["latitude"])   # Output: 40.7128
print(person["address"]["coordinates"]["longitude"])  # Output: -74.0060

# The .get() method is safer as the code won't throw an error if there is a key mistake

print(person.get("name"))  # Alice

# Nested safe access (chain .get())
print(person.get("address", {}).get("city"))                    # Wonderland
print(person.get("address", {}).get("phone"))                   # None (key doesn't exist)
print(person.get("address", {}).get("phone", "Not provided"))   # "Not provided" returned even though key doesn't exist

# deeply nested
lat = person.get("address", {}).get("coordinates", {}).get("latitude")
print(f'{lat}\n\n')  # 40.7128

# recursively iterate over key value pairs
def print_nested_dict(d, indent=0):
    for key, value in d.items():
        print("  " * indent + str(key) + ": " + str(value))
        if isinstance(value, dict):
            print_nested_dict(value, indent + 1)

print_nested_dict(person)


