class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(i):
            time = 0
            for pile in piles:
                time += math.ceil(pile / i)
            return time <= h
        
        l, r = 1, max(piles) 
        res = r
        while l <= r:
            mi = l + (r - l) // 2

            if canEat(mi):
                res = mi
                r = mi - 1
            else:
                l = mi + 1

        return res