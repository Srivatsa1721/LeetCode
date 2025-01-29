class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        # return [i for i,val in enumerate(nums) if val == target]
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res