class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r  # worst case: max(piles)

        while l <= r:
            m = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += (pile + m - 1) // m  # ceil(pile / m)

            if hours <= h:
                res = m
                r = m - 1   # try smaller speed
            else:
                l = m + 1   # need bigger speed

        return res
