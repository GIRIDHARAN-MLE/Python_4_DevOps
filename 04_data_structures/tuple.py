# Defining a Tuple.
# Tuples and Strings are immutable.

empty_tuple = ()
the_tuple = (5, 6.4, 8)

print(empty_tuple)
print(the_tuple)

print(bool(empty_tuple))
print(bool(the_tuple))

the_tuple_1 = (3, 2, [7, 6, 9], 4, 10)
print(the_tuple_1)

print(the_tuple_1[1])
print(the_tuple_1[1:])
print(the_tuple_1[2][1])

#the_tuple_1[1] = 7                     # Cannot Modify, Tuples are immutable.
#print(the_tuple_1)

the_tuple_2 = (4, 6, 5, 7, 4, 8)
print(the_tuple_2.count(4))

print(the_tuple_2.index(4))
print(the_tuple_2.index(4, 1))

print(len(the_tuple_2))

the_string = 6, 8, 5
print(the_string, type(the_string))     # BY Default it is a tuple data structure.
