# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:

print('my solution')
def merge_lists(list1, string) -> list:
    string_to_list = list(string)
    merge = list1 + string.split() + string_to_list
    return merge

print(merge_lists([1, 2, 3, 4], "Hello there!"))




# Course Solution
print('course solution')

print("")
def multi_merge(list_a, str):
    return list_a + str.split() + list(str)

print(multi_merge([1, 2, 3, 4], "Hello there!"))






































# Solution:

# def multi_merge(list_a, str):
#     return list_a + str.split() + list(str)
#
# print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
