#Bubble Sorting
#Push the maximum to the last by adjacent swaps
def bubbleSorting(num):
    #Sort the highest value at last and swap it(ascending order)
    #Time Complexity = o(n^2)
    #Space Complexity = o(1)
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
                print(temp,i,j,num)
    return num
print(bubbleSorting([7,8,3,1,2]))
#Running Loop:
# temp i j num
#8 0 1 [7, 3, 8, 1, 2]
#8 0 2 [7, 3, 1, 8, 2]
#8 0 3 [7, 3, 1, 2, 8]
#7 1 0 [3, 7, 1, 2, 8]
#7 1 1 [3, 1, 7, 2, 8]
#7 1 2 [3, 1, 2, 7, 8]
#3 2 0 [1, 3, 2, 7, 8]
#3 2 1 [1, 2, 3, 7, 8]
#[1, 2, 3, 7, 8]