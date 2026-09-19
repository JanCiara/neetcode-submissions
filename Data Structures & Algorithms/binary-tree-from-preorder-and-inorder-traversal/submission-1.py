class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        pre_i = 0

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal pre_i
            if lo > hi:
                return None

            val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(val)

            mid = idx[val]
            root.left = build(lo, mid - 1)   # najpierw lewe!
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)