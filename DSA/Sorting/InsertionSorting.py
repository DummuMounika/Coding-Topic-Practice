def insertionSorting(nums):
#Takes the element and place it in its correct order
# it sorts one item at a time by comparisons(ascending order)
# Time Complexity = o(n^2)
# Space Complexity = o(1)
    for i in range(1,len(nums)):
        current = nums[i] 
        j = i-1
        print(":1:",j,current)
        while(j >= 0 and current < nums[j]):
            nums[j+1] = nums[j]
            j-=1
            print(":2:", j,nums)
        nums[j+1] = current # nums[1]=current
        # print(":3:",nums[j+1])
        # print(":4:",i, j ,nums)
    return nums
print(insertionSorting([7,8,3,1,2]))
# Running Loops
# i j nums
# 1 0 [7,8,3,1,2]
# 2 -1 [3,7,8,1,2]
# 3 -1 [1,3,7,8,2]
# 4 0 [1,2,3,7,8]

