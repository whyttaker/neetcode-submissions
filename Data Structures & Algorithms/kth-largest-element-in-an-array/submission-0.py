class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        while len(heap) > k:
            heapq.heappop(heap)
        
        # for n in heap:
        #     n *= -1

        print(heap)

        return heapq.heappop(heap)