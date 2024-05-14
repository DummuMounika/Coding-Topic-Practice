#Selection Sorting
#Selects Mininmum and swap
class Solution:
    def select(self, arr):
        for i in range(len(arr) - 1):
            smallest = i
            for j in range(i + 1, len(arr)):
                if arr[smallest] > arr[j]:
                    smallest = j
            temp = arr[smallest]
            arr[smallest] = arr[i]
            arr[i] = temp
        return arr

    def selectionSort(self, arr, ):
        return self.select(arr)


# Example usage:
sol = Solution()
arr = [64, 25, 12, 22, 11]
sorted_arr = sol.selectionSort(arr)
print("Sorted array is:", sorted_arr)