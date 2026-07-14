# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        cur = []
        prev = 0
        q.append((root, 0))

        while q:
            node, lvl = q.popleft()
            if not node:
                continue
            if lvl > prev:
                res.append(cur)
                cur = []
                prev = lvl         

            cur.append(node.val)   
            q.append((node.left, lvl + 1))
            q.append((node.right, lvl + 1))
        if cur:
            res.append(cur)
        return res
