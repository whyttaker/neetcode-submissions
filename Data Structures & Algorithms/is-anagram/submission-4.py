class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()

        for c in s:
            seen[c] = seen.get(c, 0) + 1
        print(seen)
        for c in t:
            if seen.get(c, 0) == 0:
                return False
            seen[c] = seen.get(c, 0) - 1
        print(seen)
        for k in seen.keys():
            if seen.get(k, 0) != 0:
                return False
        return True