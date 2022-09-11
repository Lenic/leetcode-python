from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        predefined = [[1, 2, 4, 8], [1, 2, 4, 8, 16, 32]]

        def getValues(sources: List[int], n: int, max: int) -> List[int]:
            res: List[int] = []
            if len(sources) < n:
                return res

            def inner(ans: List[int], index: int):
                if len(ans) == n:
                    s = sum(ans)
                    if s <= max:
                        res.append(s)
                    return

                for i in range(index, len(sources)):
                    ans.append(sources[i])
                    inner(ans, i + 1)
                    ans.pop()

            inner([], 0)
            return res

        res: List[str] = []
        for i in range(turnedOn + 1):
            hours = [str(val) for val in getValues(predefined[0], i, 11)]
            minutes = [str(val) if val > 9 else f"0{val}" for val in getValues(predefined[1], turnedOn - i, 59)]

            if len(hours) == 0 or len(minutes) == 0:
                continue

            for h in hours:
                for m in minutes:
                    res.append(f"{h}:{m}")
        return res


# [
#     "0:03",
#     "0:05",
#     "0:06",
#     "0:09",
#     "0:10",
#     "0:12",
#     "0:17",
#     "0:18",
#     "0:20",
#     "0:24",
#     "0:33",
#     "0:34",
#     "0:36",
#     "0:40",
#     "0:48",
#     "1:01",
#     "1:02",
#     "1:04",
#     "1:08",
#     "1:16",
#     "1:32",
#     "2:01",
#     "2:02",
#     "2:04",
#     "2:08",
#     "2:16",
#     "2:32",
#     "3:00",
#     "4:01",
#     "4:02",
#     "4:04",
#     "4:08",
#     "4:16",
#     "4:32",
#     "5:00",
#     "6:00",
#     "8:01",
#     "8:02",
#     "8:04",
#     "8:08",
#     "8:16",
#     "8:32",
#     "9:00",
#     "10:00",
# ]
print(Solution().readBinaryWatch(2))

# ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
print(Solution().readBinaryWatch(1))

# []
print(Solution().readBinaryWatch(9))
