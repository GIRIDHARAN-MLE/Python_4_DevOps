# Lists are Mutable, Strings are Immutable 

the_list = []
the_list_1 = [ 6, 4.5, "devops", 3]

# bool(empty_list) = False
# bool(non_empty_list) = True

"""
print(bool(the_list))
print(bool(the_list_1))
"""

print(the_list_1[0])
print(the_list_1[2])
print(the_list_1[-1])
print(the_list_1[-2])
print(the_list_1[:])
print(the_list_1[0:])
print(the_list_1[1:3])
print(the_list_1[2][3])


the_list_1[0] = 40
print(the_list_1)

the_list_2 = [ 3, 6, 9, 6, 3, 9]

print(the_list_2.index(6))
print(the_list_2.index(6,2))

print(the_list_2.count(6))
print(the_list_2.count(9))
print(the_list_2.count(5))

the_list_3 = [5, 10, 15, 20]
the_list_3.clear()
print(the_list_3) 

the_list_4 = [80, 50, 65, 93]

the_new_list = the_list_4
the_copied_list = the_list_4.copy()

print(id(the_list_4), id(the_new_list))
print(id(the_copied_list))

print(the_list_4)
the_list_4.append(77)
print(the_list_4)
the_list_4.insert(1, 75)
print(the_list_4)

the_list_5 = [6, 8.5]
the_list_4.append(the_list_5)
print(the_list_4)

the_list_4.extend(the_list_5)
print(the_list_4)

the_list_4.remove(50)
print(the_list_4)

the_list_4.pop()
print(the_list_4)
the_list_4.pop(1)
print(the_list_4)
print(the_list_4.pop())         # pop() shows the data which is to be removed and deletes it.
print(the_list_4)

the_list_6 = [ 1, 4, 2, 3, 5 ]
the_list_6.reverse()
print(the_list_6)
the_list_6.sort()               # sort() actually arrange as ascending order.
print(the_list_6)
the_list_6.sort(reverse=True)   # for getting descending order.
print(the_list_6)
