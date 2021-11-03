"""
Maximum Sub-matrix: 2-D Kadane Algorithm
Explanation: https://www.youtube.com/watch?v=yCQN096CwWM
"""

matrix = [[ 2,  1, -3, -4,  5],
          [ 0,  6,  3,  4,  1],
          [ 2, -2, -1,  4, -5],
          [-3,  3,  1,  0,  3]]

def max_submatrix(matrix):
    """
    Time Complexity: O(col*col*row)
    """
    row, col = len(matrix), len(matrix[0])
    max_sum = float("-inf")
    max_left, max_right, max_top, max_down = -1,-1,-1,-1
    
    for left in range(col): #O(col)
        nums = [0]*row #nums is the accummulated col
        for right in range(left, col): #O(col)
            for r in range(row): #O(row)
                nums[r] += matrix[r][right]
            #print(nums)
            current_sum, max_start, max_end = max_subarray(nums) #O(row)
            if current_sum > max_sum:
                max_left, max_right, max_top, max_down = left, right, max_start, max_end
                max_sum = current_sum
            
    return max_sum, max_left, max_right, max_top, max_down-1
    
max_submatrix(matrix)
