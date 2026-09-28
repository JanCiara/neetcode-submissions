"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            new = Node(n.val)
            oldToNew[n] = new
            for nei in n.neighbors:
                new.neighbors.append(dfs(nei))
            return new

        return dfs(node) if node else None