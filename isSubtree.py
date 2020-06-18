# O(n*m) time: worst case must iterate through all of s tree, and for each node in s tree, must iterate through all of t tree.
#              Since n is the number of nodes in s tree and m is the number of nodes in t tree
#              It will take O(n*m) time for the worst case
# O(n*m) space: every time the function calls for a recursion, it is stored on the stack
#               so with the same explanation is time complexity, it comes down to O(n*m) space complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if (s and t) is None: 
            return False
        elif self.isSametree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
    def isSametree(self, s, t):
        
        if (s is None and t is not None) or (t is None and s is not None):
            return False
        elif (s and t) is None:
            return True
        elif s.val != t.val:
            return False
        else:
            return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
        