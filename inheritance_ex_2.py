                    # Inheritance constructor

class Phone:

    def __init__(self,price, brand):
        print("Inside Parent constructor")
        self.price = price
        self.brand = brand

class SmartPhone(Phone):
    pass

s= SmartPhone(5000,"Apple")

print(s.price)
print(s.brand)    
