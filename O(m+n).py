import time

large1= ['nemo' for i in range(100000)]
large2= ['nemo' for i in range(100000)]

def find_nemo(array1, array2):

    #here there are two different variables array1 and array2
    #They have to be represented by 2 different variable in the Big-O represntation as well
    #Let array1 correspond to to m and array2 correspond to n

    t0 = time.time() #O(1)
    for i in range(0, len(array1)): #O(m)
        if array1[i] == 'nemo': #m*O(1)
            print("Found Nemo!!") #k1*O(1) where k1 <= m because this statement will be executed only if the if statement returns True, which can be k1(<=m) times

    t1=time.time()
    print(f'The search took {t1-t0} seconds.')

    t0 = time.time()
    for i in range(0,len(array2)):
        if array2[i] == 'nemo':
            print("Finding Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')

find_nemo(large1,large2)