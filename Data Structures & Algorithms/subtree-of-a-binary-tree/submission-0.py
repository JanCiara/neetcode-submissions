# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def eq(a, b):
            if not a and b:
                return False
            if not b and a:
                return False
            if not a and not b:
                return True
            
            if a.val != b.val:
                return False
            return eq(a.left, b.left) and eq(a.right, b.right)

        def dfs(a, b):
            if not a:
                return False
            if eq(a, b):
                return True
            
            return dfs(a.left, b) or dfs(a.right, b)
        

        return dfs(root, subRoot)
        