class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1
        hm = 0
        lm = 0

        print("r: " + str(r) + " l: " + str(l))
        print("t: " + str(t) + " b: " + str(b))
        print("hm: " + str((t+b)//2))
        print("lm: " + str((r+l)//2))

        while t <= b:
            hm = (t+b)//2
            if hm < 0 or hm > len(matrix)-1:
                return False
            if matrix[hm][l] <= target <= matrix[hm][r]:
                break
            elif matrix[hm][r] < target:
                t = hm + 1
            elif target < matrix[hm][l]:
                b = hm - 1
        
        print(hm)

        while l <= r:
            lm = (l+r)//2
            if matrix[hm][lm] == target:
                return True
            elif matrix[hm][lm] < target:
                l += 1
            elif target < matrix[hm][lm]:
                r -= 1

        return False

