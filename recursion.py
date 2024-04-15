def countdown(i):
    print (i)
    if i<=0:
        return
    else:
        countdown (i-1)

### print (countdown(5))

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
### print (fact(5))
    
def summa(arr):
    if arr == []:
        return 0
    return arr[0] + summa(arr[1:])

    
    
### print (summa([1, 2, 3, 4, 5]))

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

### print(count([1, 2, 3, 4, 5]))

def max_(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = max_(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max
    
print (max_([1,15,47,93,15,4]))

