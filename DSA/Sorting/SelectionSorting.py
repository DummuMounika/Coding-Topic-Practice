#Selection Sorting
def selectionSorting(nums):
    # Sort the least value at first and swap it(ascending order)
    # Time Complexity = o(n^2)
    # Space Complexity = o(1)
    for i in range(len(nums)-1):
        smallest=i
        for j in range(i+1,len(nums)):
            if nums[smallest] > nums[j]:
                smallest = j

        temp = nums[smallest]
        nums[smallest] = nums[i]
        nums[i] = temp
        print(nums)
print(selectionSorting([7,8,3,1,2]))
# 1 8 3 7 2
# 1 2 3 7 8
# 1 2 3 7 8