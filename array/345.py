from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        data, vowls = list(s), set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        i, j = 0, len(data) - 1
        while i < j:
            while i < j and data[i] not in vowls:
                i += 1
            while i < j and data[j] not in vowls:
                j -= 1
            data[i], data[j], i, j = data[j], data[i], i + 1, j - 1
        return "".join(data)


# holle
print(Solution().reverseVowels("hello"))

# leotcede
print(Solution().reverseVowels("leetcode"))
