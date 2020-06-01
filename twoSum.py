# O(n) time: only need to iterate through the entire array once
# O(n) space: if the pair is at the end of the array, the dict will fill up with all values in the array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        numsDict = {}
        
        for i in range(len(nums)):
            print(i)
            print(nums[i])
            if target-nums[i] in numsDict:
                return [i, numsDict[target-nums[i]]]
            numsDict[nums[i]] = i