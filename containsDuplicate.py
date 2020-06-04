# O(n) time: only need to iterate through the entire array once
# O(n) space: if the duplicate is at the end of the array, the dict will fill up with all values in the array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numsDict = {}
        
        for n in nums:
            if n in numsDict:
                return True
            else:
                numsDict[n] = 1
        
        return False