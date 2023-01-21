from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans: List[str] = [""] * n
        for i in range(1, n + 1):
            divisible3 = i % 3 == 0
            divisible5 = i % 5 == 0
            if divisible3 and divisible5:
                ans[i - 1] = "FizzBuzz"
            elif divisible3:
                ans[i - 1] = "Fizz"
            elif divisible5:
                ans[i - 1] = "Buzz"
            else:
                ans[i - 1] = str(i)
        return ans


# ["1","2","Fizz"]
print(Solution().fizzBuzz(3))

# ["1","2","Fizz","4","Buzz"]
print(Solution().fizzBuzz(5))

# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
print(Solution().fizzBuzz(15))
