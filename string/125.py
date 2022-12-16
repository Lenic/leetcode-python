class Solution:
    def isPalindrome(self, s: str) -> bool:
        ca, cz, cA, cZ, c0, c9 = ord("a"), ord("z"), ord("A"), ord("Z"), ord("0"), ord("9")
        i, j = 0, len(s) - 1

        while i < j:
            left = -1
            while i < j:
                val = ord(s[i])
                if ca <= val <= cz or c0 <= val <= c9:
                    left = val
                    break
                elif cA <= val <= cZ:
                    left = val + 32
                    break
                i += 1

            right = -1
            while i < j:
                val = ord(s[j])
                if ca <= val <= cz or c0 <= val <= c9:
                    right = val
                    break
                elif cA <= val <= cZ:
                    right = val + 32
                    break
                j -= 1

            if left == -1 or right == -1:
                break

            if left != right:
                return False

            i += 1
            j -= 1

        return True


# False
print(Solution().isPalindrome("race a car"))

# True
print(Solution().isPalindrome("a."))

# True
print(Solution().isPalindrome(" "))

# True
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
