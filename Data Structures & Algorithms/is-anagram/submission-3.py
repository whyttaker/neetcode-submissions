class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for c in s:
            if c in t:
                t = t.replace(c, "", 1)
            else:
                return False
        print(t)
        if (len(t) == 0):
            return True
        return False
        