#Iterative Method
#Algorithm for finding a target value within a sorted array
# It works by repeatedly dividing the search interval in half.
#Time Complexity: O(logN)
#space Complexity: O(1)


def binarySearchRecursive(arr, low, high, target):

    if low <= high:
        mid = low + (high-low)//2

        #check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif target > arr[mid]:
            return binarySearchRecursive(arr,mid + 1,high,target);

        # If target is smaller, ignore right half
        else:
            return binarySearchRecursive(arr, low, mid - 1, target);

    #if target is not found
    return -1

def binarySearchIterative(arr, low, high, target):

    while low <= high:
        mid = low + (high-low)//2

        #check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif target > arr[mid]:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    #if target is not found
    return -1

#Input array
arr = [1,5,7,65,89,123]
target = 89

#Perform binary search
result = binarySearchRecursive(arr,0,len(arr)-1,target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
