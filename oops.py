class Atm:

    #Static/ Class Variable

    __counter = 1

    
    def __init__(self):
        self.__pin=""
        self.__balance = 0

        #serial number
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter +1

        self.__Menu()


    @staticmethod
    """
        we dont pass self in static method because
        static is a class variable..we dont need object for this
    """
    
    def get_counter(): 
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            if len(new_pin) == 4:
                self.__pin = new_pin
                print("Pin changed")
            else:
                if len(new_pin) > 4:
                    print("The pin in exceding 4 digit")
                else:
                    print("The pin in less than 4 digit")
        else:
            print("Not Allowed")


    

    def __Menu(self):
        user_input = input("""
                     Hello how would you like to proceed?
                     1.Enter 1 to create Pin
                     2.Enter 2 to deposite
                     3.Enter 3 to withdraw
                     4.Enter 4 to check balance
                     5.Enter 5 to exit
                     """)
        if user_input == "1":
            self.Generatepin()
        elif user_input == "2":
            self.Deposite()
        elif user_input == "3":
            self.Withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")

    def Generatepin(self):
        self.__pin = input("Enter a 4 digit pin")
        print("Pin is generated successfully")
                
    def Deposite(self):
        temp = input("Enter your 4 digit pin")
        if temp == self.__pin:
            amount  = int(input("Enter the amount you want to deposite"))
            self.__balance = self.__balance + amount
            print("The amount is deposited in your account")
        else:
            print("You have enterd invalid pin")

    def Withdraw(self):
        temp = input("Enter your 4 digit pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount you want to withdraw"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("The amount is withdrawed from your account")
            else:
                print("Insuficent fund")
        else:
            print("You have entered invalid pin")

    
            
    def check_balance(self):
        temp = input("Enter your 4 digit pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("You have entered invalid pin")








        
