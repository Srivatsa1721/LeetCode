class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l , r = 0 , 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            else:
                l = r
                r+=1
        return False
