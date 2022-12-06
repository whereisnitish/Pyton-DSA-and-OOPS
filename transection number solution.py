class TransectionID:
    def __init__(self,start_id):
        self._start_id = start_id

    def next_method(self):
        self._start_id += 1
        return self._start_id


class Account:
    transection_counter = TransectionID(100)

    def make_transection(self):
        new_trans_id = Account.transection_counter.next_method()
        return new_trans_id

a1 = Account()
a2 = Account()

print(a1.make_transection())
print(a2.make_transection())

print(a1.make_transection())

'''
Above Program is absolutely correct,
But we dont need to solve this problem using class,
we have some other way to solve this.
    
Using Iterators :- Given Below
'''


'''*************Using Iterators Solving Problem***********'''

def Iterator_Transection_Id(start_id):
    while True:
        start_id += 1
        yield start_id

t = Iterator_Transection_Id(100)

print(t)
print(next(t))
print(next(t))

class Other_Way_Account:
    transection_c = Iterator_Transection_Id(100)

    def other_make_transection(self):
        new_trans_id = next(Other_Way_Account.transection_c)
        return new_trans_id

A = Other_Way_Account()
B = Other_Way_Account()

print(A.other_make_transection())
print(B.other_make_transection())

print(A.other_make_transection())

'''*********Solving Above problem Using Iterator*************'''

import itertools
class iterator_way_account:
    transection_c  = itertools.count(300)

    def itertools_make_transection(self):
        new_trans_id =  next(iterator_way_account.transection_c)
        return new_trans_id

I = iterator_way_account()
J = iterator_way_account()

print(I.itertools_make_transection())
print(J.itertools_make_transection())

print(I.itertools_make_transection())

