"""
Kadane's Algorithm to Maximum Sum Subarray Problem
"""

# array = [-2,1,-3,4,-1,2,1,-5,4] #max_sum = 6, sub_array = [4, -1, 2, 1]
# array = [1,-3,2,1,-1]           #max_sum = 3, sub_array = [2, 1]
array = [-1,3,-2,5,-6,1]         #max_sum = 6, sub_array = [3, -2, 5]
# array =  [5,4,-1,7,8]           #max_sum = 23

def max_subarray(nums):
    """
    This version is to return max_sum of the sub-arrays
    """
    n, max_sum = len(nums), float("-inf")
    dp = [float("-inf")]*(n+1)
    
    for i in range(1, n+1):
        if nums[i-1] >= nums[i-1] + dp[i-1]:
            dp[i] = nums[i-1]
        else:
            dp[i] = nums[i-1] + dp[i-1]
        if dp[i] > max_sum:
            max_sum = dp[i]
    return max_sum

def max_subarray(nums):
    """
    This version is to return max_sum, max_start & max_end pos
    """
    n, max_sum = len(nums), float("-inf")
    max_start, max_end = -1,-1
    dp = [float("-inf")]*(n+1)
    
    for i in range(1, n+1):
        if nums[i-1] >= nums[i-1] + dp[i-1]:
            dp[i] = nums[i-1]
            if dp[i] > max_sum:
                max_sum = dp[i]
                #Restart the start & end pos to the new (i-1) pos
                max_start = max_end = i-1
        else:
            dp[i] = nums[i-1] + dp[i-1]
            if dp[i] > max_sum:
                max_sum = dp[i]
                max_end = i-1

    return max_sum, max_start, max_end+1

max_sum, max_start, max_end = max_subarray(array)
print(max_sum, array[max_start: max_end])
