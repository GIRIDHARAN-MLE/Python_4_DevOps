""" A set is a collection which is unordered, unchangeable, and unindexed.

but you can remove items and add new items, does not allow duplicate values.

And gives Unique Values. """

the_set = { 8, 2, 6, 2, 6, 8, "ci", "cd", "cd"}
print(the_set, type(the_set), bool(the_set))

the_empty_set = set({})
print(type(the_empty_set), bool(the_empty_set))

the_list = [5, 6, 5, 4, 4, 7]
the_set_1 =set(the_list)
print(the_set_1)
print(dir(the_set_1))

the_set_2 = { 3, 4, 5, 6}
the_set_3 = {5, 6, 7, 8}
the_set_2.union(the_set_3)
the_set_2.intersection(the_set_3)
