def slidingWindow(nums,k):
    wSum = 0
    mSum = 0
    for i in range(k):
        wSum += nums[i]
    print("0", wSum)
    for i in range(k,len(nums)):
        wSum = wSum - nums[i-k] + nums[i]
        print("1",wSum)
        if wSum > mSum:
            mSum = wSum
            print("max",mSum)
    return mSum
print(slidingWindow([2,9,31,-4,21,7],3))

# 1st for loop: 42
#  2nd for loop: 36
#  2nd for loop: 48
#  2nd for loop: 24
#return 48