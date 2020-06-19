# O(n) time: iterates once through
# O(1) space: store variables water, left, and right
# Uses two pointer strategy to achieve O(n) time, otherwise bruteforce way would be O(n^2) time

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        water = 0
        left = 0
        right = len(height) - 1
        
        for i in range(len(height)):
            newWater = abs(left - right) * min(height[left], height[right])
            if newWater > water:
                water = newWater
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return water