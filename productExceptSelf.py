# O(n) time: iterate through nums once
# O(1) space: store l, r variables

# import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        l = r = 1
        
        for i in range(len(nums)):
            res[i] *= l
            res[len(nums) - 1 - i] *= r
            l *= nums[i]
            r *= nums[len(nums) - 1 - i]
        
        return res
        
#         res = [1] * len(nums)
#         for i in range(len(nums)-1):
#             arr = nums[i:] + nums[:i]
#             print(arr)
#             res = np.multiply(res, arr)
#             print(res)
            
#         return np.roll(res, -1)