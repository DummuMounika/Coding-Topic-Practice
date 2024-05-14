class Solution:
    def insert(self, alist, index, n):
        #code here
        for index in range(1,n):
            current = alist[index]
            j= index-1
            while (j >=0 and current < alist[j]):
                alist[j+1] = alist[j]
                j-=1
            alist[j+1] = current
        return alist
    #Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        #code here
        alist = self.insert(alist,0, n)
        return alist
sol = Solution()
arr = [12, 11, 13, 5, 6]
n = len(arr)
sorted_arr = sol.insertionSort(arr, n)
print("Sorted array is:", sorted_arr)
