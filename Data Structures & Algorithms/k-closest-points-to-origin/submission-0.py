class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []


        for p in points:
            print(p[0]^2)
            print(p[1]^2)
            d = math.sqrt((p[0])**2 + (p[1])**2)
            if len(heap) < k:
                heapq.heappush(heap,[-d,p])
            else:
                heapq.heappush(heap,[-d,p])
                print(heap)
                heapq.heappop(heap)

        print(heap)
        for item in heap:
            res.append(item[1])

        return res