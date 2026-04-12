class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return root