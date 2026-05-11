class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs == []:
            return "[]"
        for string in strs:
            res += string
            res += "|$|"
            print(res)
        return res[: -3]


    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        return s.split("|$|")
