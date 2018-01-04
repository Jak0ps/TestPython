#!/usr/bin/python

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    for i in grades_input:
        print i

print print_grades(grades)

def grades_sum(scores):
    total = 0
    for i in scores:
        total = total + i
    return total

print grades_sum(grades)

def grades_average(grades_input):
#    return ("%.2f" % (grades_sum(grades_input) / float(len(grades_input))))
    return grades_sum(grades_input) / float(len(grades_input))

print grades_average(grades)
