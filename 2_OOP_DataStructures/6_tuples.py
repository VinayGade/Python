'''

@author: Vinay Gade
Created on 16-Feb-2018

'''
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)

print(len(list1))
print(len(tuple1))

tuple2 = ('one', 2)
print(tuple1[0])
print(tuple2[-1])     # ??

print(tuple1.index(2))
print(tuple1.count('one'))

#tuple2 [0] = 'two'                   # type immutability ...TypeError: 'tuple' object does not support item assignment
#tuple2.append('hope')                # AttributeError: 'tuple' object has no attribute 'append'

print(tuple2)
