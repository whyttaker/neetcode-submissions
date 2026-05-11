class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        arr = []
        for num, count in frequency.items():
            arr.append([count,num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res

        