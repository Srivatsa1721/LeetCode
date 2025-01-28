class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        res = [-1,-1]
        l, r = 0 , len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid
                r = mid
                while l > 0 and nums[l - 1] == target:
                    l -= 1
                while r < len(nums) - 1 and nums[r + 1] == target:
                    r += 1
                return[l , r]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res