def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest>arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(1, len(arr)+1):
        smallest_arr = findSmallest(arr)
        newArr.append(arr.pop(smallest_arr))
    return newArr

print(selectionSort([1,25,4,15,50]))