class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_max = 0
        actual_max = 0
        prev = -10000000000
        nums = sorted(nums)
        print(nums)
        for num in nums:
            if prev + 1 == num or prev -1 == num:
                curr_max += 1
                prev = num
            elif num == prev:
                print("continuing")
                continue
            else:
                if actual_max < curr_max:
                    actual_max = curr_max
                print("actual max is: " + str(actual_max) + " ending with: " + str(prev))
                curr_max = 1
                prev = num
        if actual_max < curr_max:
            actual_max = curr_max 
        return actual_max