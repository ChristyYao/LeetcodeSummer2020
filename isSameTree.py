# O(n) time: iterate through entire tree to check if both are the same
# O(n) space: keep previous nodes to return in the recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        elif (p and q) is None:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)