import random

def binary_search(list, item):
    counter = 0
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess>item:
            high = mid - 1
        else:
            low = mid + 1
        counter += 1
        print (counter)
    return None

my_list = list(range(1,129))
print (my_list)
print (binary_search(my_list, 4))



        
