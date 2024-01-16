'''

@author: Vinay Gade
Created on 14-Feb-2018

'''
my_dict = {'k1':'v1', 'k2':'v2'}
print(my_dict ['k1'])

my_dict1 = {'k1':123, 'k2':3.14, 'k3':'string'}
print(my_dict)

nested_dict = {'k1' :{'nestKey' :{'subNestKey':'value'}}}
print(nested_dict ['k1']['nestKey']['subNestKey'])

dictionary = {}
dictionary ['k1'] = 1
dictionary ['k2'] = 2
dictionary ['k3'] = 3

print('dictionary :' + str(dictionary))


print(str(dictionary.keys()))
print(str(dictionary.values()))
print(str(dictionary.items()))

dict_list = {'key1' : 1, 'key2' : [10, 20, 30], 'key3':'value3'}
print(str(dict_list.keys()))
print(str(dict_list.values()))
print(str(dict_list.items()))
