'''
Question:-
 can we crete a method on specific instance
 so from above if we want say_hello function
 Actually be a methods, so that when we call p1.say_hello
 So then it can bind function(Eg - say hello) to the instance p1


Answer : YES
Using method type
'''


from types import MethodType
class person:
    def __init__(self, name):
        self.person_name = name

p1 =person('Nitish')
p2 = person('Harish')

#Above 2 objects, and each has there own state

print(p1.__dict__)
print(p2.__dict__)

# Now create a method object and for that create a function

def say_hello(self):
    return f'{self.person_name} says Hello'

print(type(say_hello))

# Now in this function we have to pass an object which hai person_name property

print(say_hello(p1))
print(say_hello(p2))

'''
Add this function as a method to my instance.

or creating bound method:- check below
'''


p1_say_hello_bound_method = MethodType(say_hello, p1)

print(p1_say_hello_bound_method)
print(p1.__dict__)

print(p2.__dict__)

#NOTE:- As you can see, this bound Method is not in p1 or p2's namespace

#setting atrributes:-

p1.say_hello= p1_say_hello_bound_method

print(p1.__dict__)

print(hex(id(p1)))

print(p1.say_hello())

#OR

getattr(p1,'say_hello')()

