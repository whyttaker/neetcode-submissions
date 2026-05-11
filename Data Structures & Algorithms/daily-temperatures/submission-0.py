class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            print("i: " + str(i) + " t: " + str(t))
            while stack and t > stack[-1][0]:
                print("pop")
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

        