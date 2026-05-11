class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        res = 0

        while len(stones) > 1:
            big = heapq.heappop(stones)
            small = heapq.heappop(stones)

            diff = big - small
            if diff == 0:
                continue
            else:
                heapq.heappush(stones, diff)
        
        if stones:
            res = abs(heapq.heappop(stones))

        return res
            