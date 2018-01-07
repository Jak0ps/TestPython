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

