from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res: List[str] = []

        def traversal(ans: List[int], index: int, segmentIndex: int) -> None:
            if segmentIndex == 4 or index == len(s):
                if segmentIndex == 4 and index == len(s):
                    res.append(".".join(str(val) for val in ans))
                return

            if s[index] == "0":
                ans[segmentIndex] = 0
                traversal(ans, index + 1, segmentIndex + 1)
                return

            sum = 0
            for i in range(index, len(s)):
                sum = sum * 10 + ord(s[i]) - ord("0")
                if sum <= 255:
                    ans[segmentIndex] = sum
                    traversal(ans, i + 1, segmentIndex + 1)
                else:
                    break

        traversal([0] * 4, 0, 0)
        return res


# ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
print(Solution().restoreIpAddresses("101023"))

# ["0.0.0.0"]
print(Solution().restoreIpAddresses("0000"))

# ['255.255.11.135', '255.255.111.35']
print(Solution().restoreIpAddresses("25525511135"))

# [0,0,0,10]
print(Solution().restoreIpAddresses("00010"))
