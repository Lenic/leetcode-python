from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        def getValue(data: list[str]) -> int:
            map, cur, prev = Counter(data), data[0], -1
            ans, left, right, used = 0, 0, 1, False
            map[cur] -= 1
            while right < len(data):
                val = data[right]
                if val == cur and map[val] > 0:
                    map[val] -= 1
                elif val != cur and not used and map[cur] >= 1:
                    used = True
                    prev = right
                    map[cur] -= 1
                else:
                    count = right - left
                    ans = max(ans, count)
                    map[cur] += count
                    left = right = prev if prev != -1 else right
                    cur, used, prev, cur = val, False, -1, data[left]
                    map[cur] -= 1
                right += 1
            return max(ans, right - left)

        data = list(text)
        return max(getValue(data), getValue(data[::-1]))


# 4
print(Solution().maxRepOpt1("acbaaa"))

# 3
print(Solution().maxRepOpt1("aabbaba"))

# 7
print(Solution().maxRepOpt1("aabaaabaaaba"))

# 6
print(Solution().maxRepOpt1("bbababaaaa"))

# 1
print(Solution().maxRepOpt1("abcdef"))

# 5
print(Solution().maxRepOpt1("aaaaa"))

# 4
print(Solution().maxRepOpt1("aaabbaaa"))

# 6
print(Solution().maxRepOpt1("aaabaaa"))

# 3
print(Solution().maxRepOpt1("ababa"))
