class Solution:
    def reverseWords(self, s: str) -> str:
        data, n, right = list(s), len(s), 0
        while right < n:
            left = right
            while right < n and s[right] != " ":
                right += 1
            i = right - 1
            while left < i:
                data[left], data[i] = data[i], data[left]
                left, i = left + 1, i - 1
            right += 1
        return "".join(data)


# "doG gniD"
print(Solution().reverseWords(s="God Ding"))

# "s'teL ekat edoCteeL tsetnoc"
print(Solution().reverseWords(s="Let's take LeetCode contest"))
