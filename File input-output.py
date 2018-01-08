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

# Use a file handler to open a file for writing
write_file = open("text.txt", "w")
# Open the file for reading
read_file = open("text.txt", "r")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
# Try to read from the file
print(read_file.read())
read_file.close()
print(read_file.read())
#Traceback (most recent call last):
#File "python",in <module>
#ValueError: I/O operation on closed file


#The 'with' and 'as' Keywords
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

#Case Closed?
with open("text.txt","w") as my_file:
  my_file.write("Whatever")

if my_file.closed:
  my_file.close()
print(my_file.closed)