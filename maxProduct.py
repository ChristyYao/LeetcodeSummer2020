# O(n) time: iterate through nums once
# O(1) space: store maxProduct, currMax, currMin variables
# Dynamic Programming
# Keep currMin in case of double negatives

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProduct = currMax = currMin = 0
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            temp = currMax
            currMax = max(nums[i], nums[i]*currMax, nums[i]*currMin)
            currMin = min(nums[i], nums[i]*temp, nums[i]*currMin)
            
            if currMax > maxProduct:
                maxProduct = currMax
                
        return maxProduct