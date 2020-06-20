# O(1) time: at most 31 loops
# O(1) space: store nString variable

class Solution:
    def reverseBits(self, n: int) -> int:
            
        nString = str(bin(n)[2:])
        for i in range(32 - len(nString)):
            nString = '0' + nString
        
        return(int(nString[::-1], 2))