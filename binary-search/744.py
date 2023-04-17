from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left] if left < len(letters) else letters[0]


# f
print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))

# a
print(Solution().nextGreatestLetter(["a", "b"], "z"))

# c
print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))
