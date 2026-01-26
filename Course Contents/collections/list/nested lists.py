my_list: list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'banana', 'orange'], 'd']

# pick out 'banana'
print(my_list[6][1]) # the nested array starts at index 6, banana is index 1 in that array.

# pull out whole nested list
print(my_list[6][:3]) # pick start of nested index [6] and print everything to index 3

my_list: list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'banana', ['john', 'dave'], 'orange'], 'd']
print(my_list[6][2][1]) # extract dave

my_list[6][2][1] = 'roberto'# lists are mutable - change dave to roberto
print(my_list[6][2][1])


