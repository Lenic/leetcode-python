from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        data: List[str] = []
        ca, cz, cA, cZ, c0, c9 = ord("a"), ord("z"), ord("A"), ord("Z"), ord("0"), ord("9")
        for i in range(len(s)):
            val = ord(s[i])
            if ca <= val <= cz or c0 <= val <= c9:
                data.append(s[i])
            elif cA <= val <= cZ:
                data.append(chr(val + 32))
        i, j = 0, len(data) - 1
        while i < j:
            if data[i] != data[j]:
                return False
            i += 1
            j -= 1
        return True


# True
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
