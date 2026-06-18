class Solution:
    def maxArea(self, heights: List[int]) -> int:

        nums = heights
        lef = 0
        rig = 1
        ar = []
        while rig < len(nums):
            if nums[lef] < nums[rig]:
                lef+=1
                rig+=1
            elif nums[lef] >= nums[rig]:
                area = min(nums[lef],nums[rig]) * (rig - lef)
                ar.append(area)
                rig+=1
        return(max(ar))
        