# O(n) time: iterate through entire linkedlist once
# O(n) space: store values of entire linkedlist

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # for [], linkedlist with no values
        if head == None:
            return None
        # for [1], linkedlist with one value
        elif head.next == None:
            return head
        # for [1, 2], linkedlist with two values
        elif head.next.next == None:
            headNext = head.next
            headNext.next = head
            head.next = None
            return headNext
        
        # for linkedlist with more than two values
        prevNode = head
        currNode = prevNode.next
        nextNode = currNode.next

        prevNode.next = None
        
        while currNode.next != None:
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode
                nextNode = currNode.next
                # print("prevNode", prevNode)
                # print("currNode", currNode)
                # print("nextNode", nextNode)
        
        currNode.next = prevNode
        
        return currNode