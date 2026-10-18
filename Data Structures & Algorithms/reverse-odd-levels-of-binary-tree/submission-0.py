# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        lvl_to_list = {} # 1 : [1, 7]

        q = deque([root])
        cur_lvl = 0
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_lvl % 2 == 1:
                    if cur_lvl not in lvl_to_list:
                        lvl_to_list[cur_lvl] = []
                    lvl_to_list[cur_lvl].append(cur_node.val)
                if cur_node.left and cur_node.right:
                    q.append(cur_node.left)
                    q.append(cur_node.right)
            cur_lvl += 1
        
        q = deque([root])
        cur_lvl = 0
        val_idx = 0
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_lvl % 2 == 1:
                    new_val = lvl_to_list[cur_lvl][len(lvl_to_list[cur_lvl]) - 1 - val_idx]
                    cur_node.val = new_val
                if cur_node.left and cur_node.right:
                    q.append(cur_node.left)
                    q.append(cur_node.right)
                val_idx += 1
            cur_lvl += 1
            val_idx = 0

        return root

