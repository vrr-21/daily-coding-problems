def swap(x,y):
    return y,x

def moveNonPosLeft(arr):
    j = 0
    # Move all non-positive integers to the left side of the array.
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i],arr[j] = swap(arr[i],arr[j]) #TODO swap function
            j = j + 1

def solver(arr):
    moveNonPosLeft(arr)
    # Treat the element as index, and mark the element at that index as negative
    for i in range(len(arr)):
        if arr[i] - 1 < len(arr) and arr[arr[i] - 1] > 0:
            arr[arr[i] - 1] = -1 * abs(arr[arr[i] - 1])
    # Now find the first index which contains a positive element
    index = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] > 0:
            index = i
            break
    leastPositiveInt = index + 1
    return leastPositiveInt

k = solver([1, 2, 0])
print(k)