# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        left = right = False

        if self.isSameTree(root, subRoot):
            return True
        else:
            if root and subRoot:
                left = self.isSubtree(root.left, subRoot)
                right = self.isSubtree(root.right, subRoot)
        print(str(left) + " " + str(right))
        return left or right
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = right = True
        if p and q:
            if p.val == q.val:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            if p or q:
                return False

        return left and right