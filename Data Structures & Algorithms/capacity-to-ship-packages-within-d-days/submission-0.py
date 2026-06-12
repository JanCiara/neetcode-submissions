class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def simulate(capacity):
            time = 1
            cur_sum = 0
            for w in weights:
                if cur_sum + w <= capacity:
                    cur_sum += w
                else:
                    time += 1
                    cur_sum = w

            return time <= days            

        while l <= r:
            mi = l + (r - l) // 2  

            if (simulate(mi)):
                r = mi - 1
                res = mi
            else:
                l = mi + 1

        return res