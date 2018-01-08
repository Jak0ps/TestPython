#!/usr/bin/python

my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

#Write to file iterated list

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for i in my_list:
    my_file.write(str(i)+"\n")
my_file.close()

#Print output.txt content
my_file = open("output.txt","r")

print(my_file.read())
my_file.close()


#Reading Between the Lines
""" Content of text.txt
I'm the first line of the file!
I'm the second line.
Third line here, boss.
"""
my_file = open("text.txt","r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()

#PSA: Buffering Data
