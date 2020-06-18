# O(n) time: worst case, must iterate through all of s tree and t tree to find that t is a subtree of s
# O(1) space: recursion does not take up space

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
        