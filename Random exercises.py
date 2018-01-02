#!/usr/bin/python

#Exercise 1
def is_int(x):
    if not x - int(x) == 0:
        return False
    else:
        return True

print is_int(7.0)
print is_int(7.5)
print is_int(-1)

#Exercise 2
def digit_sum(n):
    total = 0
    for i in (str(n)):
        total += int(i)
    return total

digit_sum(1234)

#Another way to do the above

def digit_sum2(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

digit_sum2(1234)

