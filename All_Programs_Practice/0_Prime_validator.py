'''

@author: Vinay Gade
aim : To check whether a number is prime or not

'''


def _is_prime_(num):
    for iter in range(2, num):
        if num % iter == 0:
            print('number ' + str(num) + ' is not prime...')
            break
    else:
        print("number " + str(num) + ' is prime...')


_is_prime_(100)

'''

str(num)   # to convert num to string
int('10')  # to converr string to number

'''
