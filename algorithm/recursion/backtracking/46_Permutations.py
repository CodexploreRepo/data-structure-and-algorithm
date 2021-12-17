class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]] #nums[:] = nums.copy() return a copy of nums
        
        for idx in range(len(nums)):
            perms = self.permute(nums[:idx] + nums[idx+1:]) #Find the perms without nums[idx]
            for perm in perms:
                perm.append(nums[idx]) # [2,3]+[1] and [3,2]+[1] individually
            result.extend(perms) # [2,3,1],[3,2,1] all together into the result
        return result
