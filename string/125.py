class Solution:
    def isPalindrome(self, s: str) -> bool:
        c0, c9, ca, cz, cA, cZ = ord("0"), ord("9"), ord("a"), ord("z"), ord("A"), ord("Z")
        i, j = 0, len(s) - 1
        while i <= j:
            left = right = -1
            while i < j:
                val = ord(s[i])
                if c0 <= val <= c9 or ca <= val <= cz:
                    left = val
                elif cA <= val <= cZ:
                    left = val + 32
                if left != -1:
                    break
                i += 1
            while i < j:
                val = ord(s[j])
                if c0 <= val <= c9 or ca <= val <= cz:
                    right = val
                elif cA <= val <= cZ:
                    right = val + 32
                if right != -1:
                    break
                j -= 1
            if left == -1 or right == -1:
                break
            if left != right:
                return False
            i, j = i + 1, j - 1
        return True


# True
print(Solution().isPalindrome("a a"))

# False
print(Solution().isPalindrome("race a car"))

# True
print(Solution().isPalindrome("a."))

# True
print(Solution().isPalindrome(" "))

# True
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
