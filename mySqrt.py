# O(log(n)) time: not too sure but theres halving and sqrting going on each iteration
# O(1) space: only need curr variable

class Solution:
    def mySqrt(self, x: int) -> int:
        print(x)
        curr = x
        while curr*curr > x:
            curr = (curr + x/curr) // 2
        return int(curr)