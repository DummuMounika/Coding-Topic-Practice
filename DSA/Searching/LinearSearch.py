#Iterative Method
#Algorithm that sequentially checks each element in a collection (such as an array or list) until a match is found
#Time Complexity: O(N)
#space Complexity: O(1)

def linearSearch (arr , N, target):
    for i in range(0,N):
        if arr[i] == target:
            return i
    return -1

arr = [6,9,32,78,90,98,121]
target = 90
N = len(arr)

result = linearSearch(arr,N,target)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

