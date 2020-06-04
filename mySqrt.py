class Solution:
    def mySqrt(self, x: int) -> int:
        print(x)
        curr = x
        while curr*curr > x:
            curr = (curr + x/curr) // 2
        return int(curr)