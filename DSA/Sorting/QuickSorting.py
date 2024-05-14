#QuickSorting
#Step1: Pick a pivot and place it in correct place in sorted array
#Step2: Smaller on the left and larger on the right
#Time Complexity: O(n log n)
#Space Complexity: O(1)
class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if (low < high):
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex - 1)
            self.quickSort(arr, pIndex + 1, high)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i = low
        j = high
        while (i < j):
            while (arr[i] <= pivot) and i <= high - 1:
                i += 1
            while (arr[j] > pivot) and j >= low - 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j


sol = Solution()
arr = [12, 11, 13, 3, 2 ,7 ,6 ,1 ,8 ,3]
n = len(arr)
sol.quickSort(arr,0,(n-1))
print("Sorted array is:", arr)
