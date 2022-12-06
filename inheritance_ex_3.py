class parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(parent):

    def show(self):
        print("This is a child class")

son= Child(100)
print(son.get_num())
son.show() 
