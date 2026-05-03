class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda x: x[0])

        pending = []
        time = 0
        res = []
        idx = 0
        n = len(tasks)

        while idx < n or pending:
            while idx < n and tasks[idx][0] <= time:
                heapq.heappush(pending, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if pending:
                t, i = heapq.heappop(pending)
                time += t
                res.append(i)
            else:
                time = tasks[idx][0]

        return res