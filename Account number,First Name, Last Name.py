'''
Question:

import itertools
import numbers
from datetime import timedelta
import time


class Timezone:
    def __init__(self,name,offset_hour,offset_minutes):
        if name is none or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')
        
        self._name = str(name).strip()

        if not isinstance(offset_hour, numbers.Integral):
            raise ValueError('Hour offset must be integer.')

        if not isinstance(offset_minutes,numbers.Integral):
            raise ValueError('Minute offset must be integer.')
        
        if offset_minutes < -59 or offset_minutes >59:
            raise ValueError('Minute offset must be between -59 and 59(inclusive)')

        # for time delta sign of minute will be set to sign of hour 
        offset = timedelta(hours=offset_hour, minutes=offset_minutes)

        if offset < timedelta(hours= -12, minutes=0) or offset >timedelta(hour=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and 14:00')


        self._offset_hour = offset_hour
        self._offest_minutes = offset_minutes
        self._offest = offset

    @property
    def offset(self):
        return self._offest

    @property
    def name(self):
        return self._name
    
    def __eq__(self,other):
        return (isinstance(other,Timezone) and
                self.name ==othet.name and
                self._offset_hour == other._offset_hour and
                self._offest_minutes == other._offest_minutes)

class account:
    transaction_counter = itertools.count(100)

    def __init__(self,account_number, first_name, last_name):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

    @property
    def account_number(self):
        return self._acccount_number

    @property
    def first_name(self):
        return self._fisrt_name

    #@first_name.setter
    #def first_name(self, value):
    #    if len(str(value).strip()) == 0:
    #        raise ValueError('First name cannot be empty')
    #    self._first_name = value
    
    @first_name.setter
    def first_name(self, value):
        self.first_name = account.validate_name(value, 'First Name')
    

    @property
    def last_name(self):
        return self.last_name

    #@last_name.stter
    #def last_name(Self,value):
    #   if len(str(value).strip()) == 0:
    #       raise ValueError('Last Name cannot be empty')
    #   self._last_name = value

    @last_name.setter
    def last_name(self, value):
        self.last_name = account.validate_name(value,'Last_Name')


    @staticmethod
    def validate_name(value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        return str(value).strip()

    # above we observer that we are not using anything from instance
    # so we didn't use self and mark it as static method

try:
    a =account('12345','Nitish', '')
except ValueError as e:
    print(e)
# last name cannot be empty

try:
    a = account('12345','Nitish',None)
except ValueError as e:
    print(e)

# above test case passed, but our code is taking last name as none
#So fix it added in above code
    
'''


#Using setter in the code

from ast import Return
import itertools
import numbers
from datetime import timedelta


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) ==0:
            raise ValueError('Time zone name cannot be empty')
        
        self._strip = str(name).strip()
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')
        
        if offset_minutes < -59 or offset_minutes >59:
            raise ValueError('Offest minutes must be between -59 and 59 (inclusive)')
        
        offset = timedelta(hours=offset_hours, minutes=offset_hours)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00')
        
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset
    
    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name
    
    def __eq__(self,other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offest_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes )
    
    def __repr__(self):
        return (
                f"TimeZone(name ='{self.name}',"
                f"offset_hours = {self._offset_hours},"
                f"offest_minutes = {self._offset_minutes})")


class account:
    transaction_counter = itertools.count(100)

    def __init__(self,account_number, first_name, last_name):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def account_number(self):
        self._account_number
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value,'First Name')

    @property
    def last_name(self):
        return  self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value,'Last Name')
    

    # removing @staticmethod and going to use instance method

    def validate_and_set_name(self,attr_name, value, field_title):
        if value is None or len(str(value).strip()) ==0:
            raise ValueError(f'{field_title} cannot be empty,')
        setattr(self,attr_name, value)
    
try:
    a = account('12345','Nitish','Kumar')
except ValueError as e:
    print(e)

print(a.first_name)
print(a.last_name)
print(a.account_number)
