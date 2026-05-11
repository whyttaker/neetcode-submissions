class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        pattern = r'[^a-zA-Z0-9]'

        # Replace all non-alphanumeric characters with an empty string
        s = re.sub(pattern, '', s)
        s = s.lower()
        print(s)
        for i in range(len(s)):
            negi = (i+1) * -1
            print(s[i] + " " + s[negi])
            if s[i].lower() != s[negi].lower():
                return False
        return True
        