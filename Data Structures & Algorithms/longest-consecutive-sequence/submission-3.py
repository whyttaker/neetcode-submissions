class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        res = 0

        snums = sorted(nums)
        print(snums)

        for num in snums:
            if num in seen:
                continue
            if not seen or seen and num-1 in seen :
                print("1")
                seen.add(num)
                count +=1 
            else:
                print("2")
                seen = set()
                count = 0
                seen.add(num)
                count +=1 
            res = max(count, res)

        
        return res