# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.findDepth(root.left, 0), self.findDepth(root.right, 0))
        
    
    def findDepth(self, root: Optional[TreeNode], depth: int) -> int:
        depth += 1
        if root is None:
            return depth
        return max(self.findDepth(root.left, depth), self.findDepth(root.right, depth))