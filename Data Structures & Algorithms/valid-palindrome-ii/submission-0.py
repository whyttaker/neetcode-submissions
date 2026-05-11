class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.regularPalindrome(s) or self.irregularPalindrome(s)
        

    def regularPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

    
    def irregularPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-2
        isPalindrome = False
        for i in range(len(s)):
            string = s[:i] + s[i + 1:]
            while l <= r:
                if string[l] != string[r]:
                    break
                l += 1
                r -= 1
            if r <= l:
                return True
        return False
        
        