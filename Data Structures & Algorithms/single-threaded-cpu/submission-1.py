class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda x: x[0])

        time = tasks[0][0]
        res = []
        pending = []
        i = 0

        while pending or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(pending, (tasks[i][1], tasks[i][2]))
                i += 1
            if pending:
                proc, idx = heapq.heappop(pending)
                time += proc
                res.append(idx)
            else:
                time = tasks[i][0]



        return res