import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # print(nums)
        # print(nums[1:]+nums[:1])
        res = [1] * len(nums)
        for i in range(len(nums)-1):
            arr = nums[i:] + nums[:i]
            print(arr)
            res = np.multiply(res, arr)
            print(res)
            
        return np.roll(res, -1)