# O(n) time: needs to iterate through entire nums array
# O(1) space: only needs to keep currSum and maxSum variables

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = nums[0]
        maxSum = nums[0]
        
        for n in nums[1:]:
            currSum = max(n, currSum + n)
            maxSum = max(maxSum, currSum)
            print(n)
            print(currSum)
            print(maxSum)
        
        return maxSum
            