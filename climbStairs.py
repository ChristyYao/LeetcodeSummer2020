# O(n) time: iterate through all n's
# O(1) space: store 'store' variables

class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Fibonacci question
        
        store = [1, 2]
        count = 3
        
        if n == 1:
            return store[0]
        
        while count <= n:
            temp = store[0]
            store[0] = store[1]
            store[1] = store[1] + temp
            count += 1
            
        return store[1]