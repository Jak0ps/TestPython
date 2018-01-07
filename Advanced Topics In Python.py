#!/usr/bin/python

my_dict = {
    "Name": "Jacob",
    "Age": 34,
    "Male": True
}

for key in my_dict:
    print key, my_dict[key]

print my_dict.items()
print my_dict.viewitems()
print my_dict.keys()
print my_dict.viewkeys()
print my_dict.values()
print my_dict.viewvalues()

for number in range(5):
    print number,

d = {
    "name": "Eric",
    "age": 26
}

for key in d:
    print key, d[key],

for letter in "Eric":
    print letter,  # note the comma!

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

my_list = range(51)
print my_list

new_list = [x for x in range(1, 6)]
print new_list

doubles = [x * 2 for x in range(1, 6)]
print doubles

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print doubles_by_3

even_squares = [x*x for x in range(1, 12) if (x*x) % 2 == 0]
print even_squares

c = ['C' for x in range(5) if x < 3]
print c

cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
print cubes_by_four

#List Slicing Syntax
l = [i ** 2 for i in range(1, 11)]
print l
print l[2:9:2]

#Omitting Indices
my_list = range(1, 11)
# Printing odd numbers
print my_list[::2]

#Reversing a List
my_list = range(1, 11)
backwards = my_list[::-1]
print backwards

#Stride Length
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

#Stride calc
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[(len(to_21)/3):((len(to_21)/3)*2):]
print odds
print middle_third

#Anonymous Functions / functional programming
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

#Lambda Syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

#Lambda example
cubes = [x ** 3 for x in range(1, 11)]
print filter(lambda x: x % 3 == 0, cubes)

#Lambda example
squares = [x*x for x in range(1,11)]
print filter(lambda x:x >= 30 and x <= 70, squares)

#Iterating Over Dictionaries
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}
print filter(lambda x:x , movies.items())

#Comprehending Comprehensions
threes_and_fives = [x for x in range(1,16) if x % 3 ==0 or x % 5 ==0 ]
print threes_and_fives

#String List Slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

#Lambda Expressions on String
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:not x == "X" ,garbled)
print message