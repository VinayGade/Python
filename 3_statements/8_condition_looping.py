'''

@author: Vinay Gade
Created on 16-Feb-2018

'''
#nested if else
radius = float(input())
PI = 3.14
if PI == 3.14:
    if radius > 10:
        print(PI * radius * radius)
    else:
        print('PI is wrong...')

#if elif else
age = int(input())
if age<10:
    print('Kid')
elif age >= 10 and age <= 30:
    print('Young')
else:
    print('Old')

#for
l = [1,2,3,4,5]
for num in l:
    print(num)





