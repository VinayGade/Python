'''

@author: Vinay Gade
Created on 19-Feb-2018

'''


def binary_search(list, key, low, high):
    if low <= high:
        mid = int((low + high)/2)
        if key == int(list[mid]):
            return list.index(key)
        elif key < int(list[mid]):
            binary_search(list, key, low, mid-1)
        else:
            binary_search(list, key, mid+1, high)

    else:
        return -1


count = int(input())
list_num = []

'''
for x in range(0, count):
    num = int(input().split())
    list_num += num
'''

nums = input().split()
for x in nums:
    list_num.append(x)

key = int(input())

print(str(key) + "found at :")
binary_search(list_num, key, 0, count-1)
