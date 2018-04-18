class Solution:
    def minNumberInRotateArray(self, rotateArray, rotate_from):
        N = len(rotateArray)
        rotate_from -= 1  # 2 -> 1
        newArray = []
        newArray[0:N - rotate_from] = rotateArray[rotate_from:N - 1]


a = Solution()
l = [1, 2, 3, 4, 5, 6]
a.minNumberInRotateArray(l, 2)
