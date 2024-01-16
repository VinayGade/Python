'''
Created on 05-Feb-2018

@author: Vinay Gade
'''
print("Welcome To Python 3 Programming")
print('Welcome To Python 3 ')

#operators

#arithmetic
print(3+5)
print(12%4)
print(5^2)   # bitwise Ex-OR
print(3/2)

# some numerical operations with use of arithmetic operators { **, //}
print( 2 ** 3 )             # Math.pow(2,3);  ...in Java
print (4 ** 0.5)            # Math.sqrt(4)
print( 5 * 'Hello ')        # for(int i=0; i<5; i++)  System.out.print("Hello ");    ...in Java
print( '$' * 5)

print( 4 // 2 )             # floor division  4 // 2 = 2
                            # division        4 / 2 = 2.0

print (7 // 3)              # int
print (7 / 3)               # float

print(round(2.676, 2))

#logical
print(8>20)
print(32>=31)
print(True)
print(False)
print( 30>=31 and 8>20)
print( 8>20 or 32>=31)
pi =3.14
print(not pi != 3.14)
print(not True)
print(not False)

#BitwiseOperators
print(2<<4)
print(64>>2)
print(8 & 10)
print(1 | 0)
print(1 & 0)
print(10 ^ 8)

length = float(input('Enter length :'))
breadth = float(input('Enter breadth :'))
area = int(length * breadth)
print(area)
