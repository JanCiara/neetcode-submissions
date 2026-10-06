class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)] # parent[1] = 1 etc.
        self.size = [1 for _ in range(n + 1)]
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.size[pu] > self.size[pv]:
            pu, pv = pv, pu
        # pv >= pu
        self.parent[pu] = pv
        self.size[pv] += self.size[pu]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        dsu = DSU(n)
        res = 0
        edges = []
        def calcDist(a, b):
            return abs((a[0] - b[0])) + abs((a[1] - b[1]))

        for i in range(n):
            pa = points[i]
            for j in range(i + 1, n):
                pb = points[j]
                dist = calcDist(pa, pb)
                edges.append((dist, i, j))
        edges.sort()

        for cur_dist, i, j in edges:
            if dsu.union(i, j):
                res += cur_dist

        return res