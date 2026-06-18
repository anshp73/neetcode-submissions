class Solution:
    def maxArea(self, heights: List[int]) -> int:

        height = heights

        lef = 0
        rig = len(height) - 1
        mx = 0

        while lef < rig:
            area = min(height[lef], height[rig]) * (rig - lef)
            mx = max(mx, area)

            if height[lef] < height[rig]:
                lef += 1
            else:
                rig -= 1

        return(mx)
        