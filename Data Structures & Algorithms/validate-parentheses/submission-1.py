class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {')': '(', '}': '{', ']' : '['}

        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                if stack:
                    pop = stack.pop()
                else:
                    return False
                if corresponding[c] != pop:
                    return False
        return not stack



