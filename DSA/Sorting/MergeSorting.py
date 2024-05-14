#Merge Sorting
#Divide and Merge
#Time Complexity: O(n log n)
#Space Complexity: O(n)
class Solution:
    def merge(self, arr, l, m, r):
        temp = []
        left = l
        right = m + 1
        # code here
        # storing elements in the temporary array in a sorted manner
        while (left <= m and right <= r):
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        # if elements on the left half are still left
        while left <= m:
            temp.append(arr[left])
            left += 1
        # if elements on the right half are still left
        while right <= r:
            temp.append(arr[right])
            right += 1
        # transfering all elements from temporary to arr
        for i in range(l, r + 1):
            arr[i] = temp[i - l]
        return arr

    def mergeSort(self, arr, l, r):
        # Base Case
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(arr, l, m)  # left half
        self.mergeSort(arr, m + 1, r)  # right half
        self.merge(arr, l, m, r)  # merging sorted halves
        return arr

sol = Solution()
arr = [12, 11, 13, 5, 6 ,9 ,6 ,5 ,2 ,3]
n = len(arr)
sorted_arr = sol.mergeSort(arr,0,(n-1))
print("Sorted array is:", sorted_arr)
