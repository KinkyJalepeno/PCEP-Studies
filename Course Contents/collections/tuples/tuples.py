my_tuple: tuple = ('a', 'b', 'c', 'd', [1, 2, 3, 4], 'e', 'f')

# tuples once created are immutable but can contain anything just like lists
# If the tuple contains a list however, values within can be reassigned.

my_tuple[4][2]: list = 'a'
print(f'Now we see "a" has replaced 3 in the nested list" - {my_tuple}')

# but the list as a whole cannot be changed as the list itself belongs to the tuple
# example - we cannot do my_tuple[4] = [4, 5, 6] - we would have to change each list entry one by one

# all the usual list methods like count etc work with tuples
