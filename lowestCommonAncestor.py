# O(log(n)) time: worst case p and q are in the lowest level of the tree,
#                 then the time is halving during each recursion to get to p and q
# O(log(n)) space: worst case p and q are in the lowest level of the tree,
#                  then the space will be the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root