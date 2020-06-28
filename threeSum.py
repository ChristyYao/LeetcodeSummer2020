# O(nm) time: nested for loop      * not too sure *
# O(n) space: store sets in numSet

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        numsSet = set()
        
        for i in range(len(nums) - 2):
            subSet = set()
            twoSum = 0 - nums[i]
            
            for j in range(i+1, len(nums)):
                if twoSum - nums[j] in subSet:
                    numsSet.add((nums[i], twoSum - nums[j], nums[j]))
                else:
                    subSet.add(nums[j])
                    
        return list(numsSet)