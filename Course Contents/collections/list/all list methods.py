# all list methods

lst = [3, 1, 4, 1, 5]

# All list methods
lst.append(9)               # [3, 1, 4, 1, 5, 9] - Added a 9 on the end
lst.extend([2, 7])          # [3, 1, 4, 1, 5, 9, 2, 7] - added a 2 and a 7 to the end
lst.insert(0, "hello")     # ["hello", 3, 1, 4, 1, 5, 9, 2, 7] - insert x in index y
lst.remove(1)               # removes first 1 → ["hello", 3, 4, 1, 5, 9, 2, 7]
x = lst.pop()               # x = 7, list becomes ["hello", 3, 4, 1, 5, 9, 2]
lst.clear()                 # [] - erases list contents
len(lst)                    # gets length of a list



lst = [10, 20, 10, 30]

print(lst.index(20))        # 1 - returns index of searched value
print(lst.count(10))        # 2
lst.sort()                  # [10, 10, 20, 30] also words on strings
lst.reverse()               # [30, 20, 10, 10] also words on strings
new = lst.copy()            # shallow copy

lst[0]: list = 'word'           # assign word to index 0
print(lst)

# LISTS CAN BE SLICED LIKE STRINGS !!