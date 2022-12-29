class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store: dict[str, int] = {}
        for val in s:
            if val in store:
                store[val] += 1
            else:
                store[val] = 1
        for val in t:
            if val not in store:
                return False
            count = store[val]
            if count == 1:
                store.pop(val)
            else:
                store[val] = count - 1
        return True if len(store) == 0 else False


# false
print(Solution().isAnagram(s="rat", t="car"))

# true
print(Solution().isAnagram(s="anagram", t="nagaram"))
