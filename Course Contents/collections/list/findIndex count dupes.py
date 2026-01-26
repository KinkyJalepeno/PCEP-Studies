my_list: list = ['a', 'b', 'c', 'd', 'e', 'c']

# find the index of c
c_location = my_list.index('c') # output 2 - will give index of the first matching value.
print(f'Index of first C is: {c_location}')


# find index of each occurrence of "c"
for index, value in enumerate(my_list):
    if value == 'c':
        print(f'found a "c" in index {index}')

# count number of C's in list
c_count = my_list.count('c') # this is case-sensitive
print(f'There are {c_count} C\'s in the list')



