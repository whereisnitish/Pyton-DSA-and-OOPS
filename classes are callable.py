class MyClass:
    pass

my_obj =MyClass

print(my_obj)

my_obj = MyClass()
print(my_obj)


print(type(my_obj))

print(isinstance(my_obj,MyClass))

# ***********Instantiating class
'''

When we call a class, a class instance object is created 
This class instance object has its own NAMESPACE
This object has some attributes, python automatically implement to us

__dict__ :- Object local namespace
__class__ :- tells us which class was used to instantiate the obj.

'''

print(my_obj.__dict__)

print(MyClass.__dict__)
