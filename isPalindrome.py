# O(n/2) time: iterate through string until p1 and p2 cross over
# O(1) space: only need to keep p1, p2 variables

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            print(p1, s[p1], p2, s[p2])
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
            
        return True