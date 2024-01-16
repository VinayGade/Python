'''
@author : Vinay Gade
Python program to print reverse fibonacci series upto n
'''
def _reverse_fibonacci_(number):
    series = []
    series += [0]
    series += [1]
    for iter in range(2,number):
        series [iter] = series[iter - 2] + series[iter - 1]
    '''
    for i in range(number-1, -1, -1):
        print(series[i])
    '''
n = int(input())
_reverse_fibonacci_(n)
