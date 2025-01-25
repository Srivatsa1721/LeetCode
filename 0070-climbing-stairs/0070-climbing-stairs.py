class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev2 , prev1 =  1 , 1
        for i in range(2, n + 1):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current
        return prev1