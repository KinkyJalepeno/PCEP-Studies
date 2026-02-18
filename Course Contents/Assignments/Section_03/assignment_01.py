# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

def merged_lists(list1, list2) -> list:
    for item in list2:
        list1.append(item)
    return list1

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print(merged_lists(list1, list2))


# course solution:

def merge_lists(list_a, list_b):
    return list_a + list_b

my_list = merge_lists([1, 2, 3], ['a', 'b', 'c'])
print(my_list)
