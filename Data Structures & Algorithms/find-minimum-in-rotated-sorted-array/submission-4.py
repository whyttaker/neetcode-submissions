class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = max(nums)
        while l < r:
            m = (l + (r-1)) // 2

            res = min(res, nums[m])
            if nums[m] < nums[r]:
                r = m
                
            else:
                l = m + 1
        return nums[l]

