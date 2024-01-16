'''
symbol pattern 1

*
* *
* * *
* * * *
* * * * *

'''

'''
symbol pattern 2

* * * * *
* * * *
* * *
* *
*

'''

def _print_symbol_1(number):
    for iter in range(0,number):
        for in_iter in range(0, iter + 1):
            print("* ",end="")

        print("\r")


def _print_symbol_2(num):
    for i in range(0, num):
        for j in range(num, i-1, -1):
            print('* ',end='')
        print('\r')

print(_print_symbol_1(5))

print('Print symbol pattern 2')

print(_print_symbol_2(5))
