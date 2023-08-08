the_empty_dict = {}
print(the_empty_dict, type(the_empty_dict), bool(the_empty_dict))

""" Dictionaries are used to store data values in key:value pairs.
 A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""

the_dict = {"fruit":"apple", "animal":"dog", 2:"two", "three":3}
#print(the_dict)
#print(the_dict['fruit'])
#print(the_dict.get('animal'))
#print(the_dict['four'])
#print(the_dict.get('four'))

#the_dict.clear()
#print(the_dict)

"""
the_dict['scripting'] = 'python'
print(the_dict)
the_dict['scripting'] = 'shell'
print(the_dict) """

"""
print(the_dict.keys())
print(the_dict.values())
print(the_dict.items())

the_copy_dict = the_dict.copy()
print(the_copy_dict)
print(id(the_dict), id(the_copy_dict)) """

the_dict_1 = {'ci':'jenkins'}
the_dict.update(the_dict_1)
print(the_dict)

""" The popitem() method removes the item that was last inserted into the dictionary.
In versions before 3.7, the popitem() method removes a random item.
The removed item is the return value of the popitem() method, as a tuple """

#the_dict.pop('three')
#print(the_dict)
#the_removed_item = the_dict.popitem()  
#print(the_dict)
#print(the_removed_item)

"""
the_keys = [ 'ci', 'cd', 'iac', 'cloud' ]
dict_keys = dict.fromkeys(the_keys)
print(dict_keys)

dict_keys['ci'] = "gitlab"
dict_keys['cd'] = "docker_ansible"

print(dict_keys) """

no_keys = {}
no_keys.setdefault('cd', 'docker')
print(no_keys)

the_keys_1 = { 'iac':'terraform' }
the_keys_1.setdefault('iac', 'ansible')
print(the_keys_1)

