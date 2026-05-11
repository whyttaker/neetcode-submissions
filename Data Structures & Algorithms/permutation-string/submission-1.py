class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1
        freq = {}
        for c in s1:
            freq[c] = freq.get(c,0) + 1
        while r < len(s2):
            temp = freq.copy()
            for i in range(l,r+1):
                print(i)
                print(s2[i])
                count = temp.get(s2[i], 0)
                if count == 0:
                    break
                elif count == 1:
                    del temp[s2[i]]
                elif count > 1:
                    temp[s2[i]] = temp.get(s2[i], 0) - 1
            print(temp)
            if not temp:
                return True
            l += 1
            r += 1
        return False
        