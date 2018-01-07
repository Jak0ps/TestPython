#!/usr/bin/python

class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)
    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

#My Example
class Employee(object):
    def __init__(self, name, id, team, manager):
        self.name = name
        self.id = id
        self.team = team
        self.manager = manager
    def print_welcome(self):
        print "Welcome %s to our company, your ID is %s, and you are hired for %s" % (self.name, self.id,self.team)
    def is_manager(self):
        if self.manager:
            print "you are the manager of the %s team" % (self.team)
        else:
            print "Your manager will contact you later"

worker = Employee("Jacob", "21234234", "Devops", False)
mangr = Employee("Moshe", "21632232", "Devops", True)


worker.print_welcome()
worker.is_manager()
mangr.print_welcome()
mangr.is_manager()

#Class Syntax
#This is an empty class
class Animal(object):
    pass

#Animal Class
class Animal(object):
    def __init__(self, name):
        self.name = name
zebra = Animal("Jeffrey")
print zebra.name

#Example
# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

#Class Scope
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive


#Example

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Johny",6)
hippo.description()
