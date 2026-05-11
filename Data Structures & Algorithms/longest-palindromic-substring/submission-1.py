class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, length = 0, 0

        for i in range(len(s)):
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r-l+1 > length:
                    start = l
                    length = r-l+1
                l -= 1
                r += 1


            l, r = i, i+1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r-l+1 > length:
                    start = l
                    length = r-l+1
                l -= 1
                r += 1

        return s[start: start+length]