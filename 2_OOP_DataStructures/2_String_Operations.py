'''
Created on 06-Feb-2018

@author: Vinay Gade
'''

"Python 3 is the simplest OO Progrmming languagae."
new_string = 'Python 3 Programming'             # declaration of string 'new_string'
new_string_array = new_string.split()           # declaration of string array 'new_string_array'
print(new_string)
print(new_string_array)
print('new_string[4] : '+ new_string[4])                            # in Java :: new_String.charAt(4)
                                                                    # in Java String :: "a"+"b" = "ab"

print('new_string_array[2] : '+ new_string_array[2])

capitalize_string = new_string.capitalize()
print('capitalize_string : '+ capitalize_string)

upper_string = new_string.upper()
print('upper_string : '+ upper_string)

lower_string = new_string.lower()
print('lower_string : ' + lower_string)

formatting_string = "Simplest Programming Language :{}".format("Python 3")
print('formatting_string : ' + formatting_string)

pet_list_string = "I have 3 Pets one {} and two {}".format('Dog','cat')
print('pet_list_string : ' + pet_list_string)

#pet_list_string_placeholders = "I have 3 Pets one {x} and two {y}".format('Dog','cat')  #KeyError: 'x'

pet_list_string_placeholders = "I have 3 Pets one {x} and two {y}".format(x='Dog',y='cat')
print('pet_list_string_placeholders : ' + pet_list_string_placeholders)

#print(x)    #NameError: name 'x' is not defined
#print(y)

grade = input()
print("Unknown grade {0} being ignored : ".format(grade))

number_series = '0123456789'
print('number series from location 7 : ' + number_series[7:])
print('number series upto index 6 : ' + number_series[:6])
print('number series from 3 to 7 : '+ number_series[3:7])
print('number series with step 2 (alternate characters ) : ' + number_series[::2])

total_points = 6
num_courses = 3
print('Your GPA is {0:.2} : '.format(total_points / num_courses))

str1 = "javatpoint"
str2 = 'sssit'
str3 = "seomount"
str4 = 'java'
str5 = "int"
str6 = "seo"

print('str2 not in str1 : ' + str2 not in str1)     # !str1 . contains (str2) ...Java
print('str4 in str1 : ' + str4 in str1)             # !str1 . contains (str4) ...Java
print('str5 not in str1 : ' + str5 not in str1)

