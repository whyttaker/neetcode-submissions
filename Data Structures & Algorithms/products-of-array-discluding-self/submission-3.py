class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = 1

        for n in nums:
            res.append(prefix)
            prefix *= n
        
        postfix = 1
        print(res)
        print(nums)
        for i, value in reversed(list(enumerate(nums))):
            print(i)
            res[i] *= postfix
            postfix *= nums[i]

        return res
        