import numbers
from datetime import timedelta
from time import time

class TimeZone:
    def __init__(self,name, offset_hours,offset_minutes):
        if name is None or len(str(name)) == 0:
            raise ValueError("Time Zone can't be empty.")

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be Integer')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minute offset must be Integer')
        
        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError('Minutes offset must be between -59 to 59')

        offset  = timedelta(hours=offset_hours, minutes= offset_minutes)
        if offset < timedelta(hours= -12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00')


        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset  = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self,other):
        return (isinstance(other, TimeZone)and 
        self.name == other.name and
        self._offset_hours == other._offset_hours and
        self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return(f"TimeZone(name= '{self.name}',"
               f"Offset_hour ='{self._offset_hours}', "
               f"Offset_minutes = '{self._offset_minutes})' ")


#Unit Test

tz1 = TimeZone('ABC',-2,-15)

print(tz1.name)

print(tz1.__dict__)

from datetime import datetime

dt = datetime.utcnow()
print(dt)

print(dt + tz1.offset)
# Output will decrease it by -2 and -15

try:
    tz =TimeZone('',0,0)
except Exception as e:
    print(e)

#Timezone name can not be empty
