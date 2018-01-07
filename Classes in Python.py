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


#Class Variables
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Johny",6)
sloth = Animal("Jo",8)
ocelot = Animal("Jee",14)
print hippo.health
print sloth.health
print ocelot.health

#Real world code
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
#Adding Banana to my shopping cart
my_cart = ShoppingCart("Jacob")
my_cart.add_item("Banana",14)

#Class Inheritance , look at the class name and the "object" of the 2nd class
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#Inheritance syntax
"""
In Python, inheritance works like this:

class DerivedClass(BaseClass):
  # code goes here
  
where DerivedClass is the new class you're making and BaseClass is the class from which that new class inherits.
"""

class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

#Override in class
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name

class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

#Example of super call
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Jacob")
print milton.full_time_wage(10)
print milton.calculate_wage(10)


#Class Basics
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        Triangle.angle1 = angle1
        Triangle.angle2 = angle2
        Triangle.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

#CodeAcademy code
class Triangle2(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

tri = Triangle(90,90,90)
tri2 = Triangle2(90,90,90)
print tri.check_angles()
False
print tri2.check_angles()
False
tri = Triangle(60,60,60)
tri2 = Triangle2(60,60,60)
print tri.check_angles()
True
print tri2.check_angles()
True

tri3 = Triangle(90,30,60)
print tri3.number_of_sides
print tri3.check_angles()
