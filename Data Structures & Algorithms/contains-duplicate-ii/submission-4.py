class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        while r <= len(nums):
            seen = set()
            for i in range(l, r):
                if nums[i] in seen:
                    return True
                else:
                    seen.add(nums[i])
            if r < k+1:
                r += 1
            else:
                
                l += 1
                r += 1

        return False