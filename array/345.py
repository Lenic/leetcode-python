from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        q, stack, ans, vowels = deque([]), deque([]), [], set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        for i, val in enumerate(s):
            ans.append(val)
            if val in vowels:
                q.append(i)
                stack.append(val)
        while len(q):
            ans[q.popleft()] = stack.pop()
        return "".join(ans)


# holle
print(Solution().reverseVowels("hello"))

# leotcede
print(Solution().reverseVowels("leetcode"))
