"""
    "pop" - Retrieve the item at index x and also removes it from sequence.
    By default, the last item in sequence is removed and returned.
"""

my_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'my_list of 1 to 10: {my_list}')

print('\n.pop() automatically "pops" out last entry of a list and removes it.')
print(f'using my_list.pop() {my_list.pop()} is removed from the list.')

print('\nThe list now ends at 9')
print(my_list) # output [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('\nwe can pop at a specific index with my_list.pop(2) for index 2 for example')
my_list.pop(2)
print(f'{my_list} - we see 3 is missing as it was index 2)') # output [1, 2, 4, 5, 6, 7, 8, 9]
