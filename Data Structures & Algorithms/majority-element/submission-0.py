class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = dict()
        halfsize = len(nums) / 2
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
            if seen[n] > halfsize:
                return n
        
        return 0