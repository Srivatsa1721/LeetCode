class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [num for num in nums if num % 2 == 0]
        if not even: 
            return -1
        count = Counter(even)
        return min(count, key=lambda x: (-count[x], x))

