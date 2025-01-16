class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        count = 0
        for num in nums:
            if num == target:
                count += 1
                if count > n //2:
                    return True
        return False