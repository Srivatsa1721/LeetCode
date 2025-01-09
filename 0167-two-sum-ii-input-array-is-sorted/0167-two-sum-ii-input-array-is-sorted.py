class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , num in enumerate(numbers):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement] + 1, i + 1]
            else:
                hashmap[num] = i
        return None 
        