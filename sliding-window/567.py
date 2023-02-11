class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        original, cur, initialValue = [0] * 26, [0] * 26, ord("a")
        for i in range(len(s1)):
            original[ord(s1[i]) - initialValue] += 1
            cur[ord(s2[i]) - initialValue] += 1
        if original == cur:
            return True
        for i in range(len(s2) - len(s1)):
            cur[ord(s2[i]) - initialValue] -= 1
            cur[ord(s2[i + len(s1)]) - initialValue] += 1

            if original == cur:
                return True
        return False


# False
print(Solution().checkInclusion(s1="ab", s2="a"))

# True
print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))

# False
print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
