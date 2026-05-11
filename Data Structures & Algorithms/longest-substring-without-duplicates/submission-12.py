class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 1
        res = 0
        seen = set()
        if s == "":
            return 0
        seen.add(s[l])
        while r < len(s):
            if s[r] in seen:
                res = max(res, len(seen))
                seen = set()
                l += 1
                r = l+1
                seen.add(s[l])
                print("adding " + str(s[l]) + " in if")
                print("l is " + str(l) + " and r is " + str(r))
                

            else:
                
                seen.add(s[r])
                print("adding " + str(s[r]) + " in else")
                r += 1

        res = max(res, len(seen)) 
        return res




        