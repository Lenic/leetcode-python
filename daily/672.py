class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1

        if n == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4

        if presses == 1:
            return 4
        elif presses == 2:
            return 7
        else:
            return 8


# 2
print(Solution().flipLights(1, 1))

# 3
print(Solution().flipLights(2, 1))

# 4
print(Solution().flipLights(3, 1))

# 8
print(Solution().flipLights(4, 100))
