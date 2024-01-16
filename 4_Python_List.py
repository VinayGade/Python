'''
Created on 08-Feb-2018

@author: Vinay Gade
'''
from builtins import print

my_list = [1,2,3]
print(my_list)

mix_list = [1,"Python3",1.2,'o']
print(len(mix_list))

print(mix_list[1])
mix_list + ['Java_SE8']
print(mix_list[1:])
print(mix_list)

mix_list = mix_list + ['Java_SE8']
print(mix_list)

mix_list.append('Spring 4')
print(mix_list)
print(mix_list.pop())

print(mix_list)

x=mix_list.pop(0)
print(mix_list)

#print(mix_list[100])

numbers_list = [100,20,30,50,40]
print(numbers_list)

numbers_list.reverse()
print(numbers_list)

numbers_list.sort()
print(numbers_list)

#creating matrix

list_1 = [10, 20, 30]
list_2 = [40, 50, 60]
list_3 = [70, 80, 90]
matrix = [list_1, list_2, list_3]      # 2D array

print(matrix)
print(matrix[1][1])

first_column = [row[0] for row in matrix]
second_column = [row[1] for row in matrix]
third_column = [row[2] for row in matrix]
print(first_column)
print(second_column)
print(third_column)

transpose_matrix = [first_column, second_column, third_column]
print(transpose_matrix)

list_1.sort()
print(list_1)

list_1.reverse()
print(list_1)

list_1.reverse()
print(list_1)

list_1_copy = []
#list_1.copy(list_1_copy)     wrong
list_1_copy = list_1[:]
#  way 1
list_1_copy= list_1_copy . copy(list_1)   # way 2
print(list_1_copy)

sum = 10+20
list_misc = [1 , "Two", '#3', 4 , 'a', '+', sum]

print(list_misc)
#list_misc.sort()
print(list_misc)



