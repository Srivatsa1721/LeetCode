class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        leftmax = height[l]
        rightmax = height[r]
        water = 0
        
        while l < r:
            if height[l] <= height[r]:
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    water += leftmax - height[l]
                l += 1
            else:
                if height[r] >= rightmax:
                    rightmax = height[r]
                else:
                    water += rightmax - height[r]
                r -= 1
                
        return water
