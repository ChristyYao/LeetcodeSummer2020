# O(n) time: iterate through linkedlist
# O(n) space: dictionary keeps all linkedlist values

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None:
            return False
        elif head.next == None:
            return False
        
        listDict = {}
        curr = head
        
        while curr.next != None:
            if curr in listDict:
                return True
            else: 
                listDict[curr] = 1
            curr = curr.next
        return False