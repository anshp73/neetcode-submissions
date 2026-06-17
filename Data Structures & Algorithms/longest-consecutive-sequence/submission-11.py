class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        se = set(nums)

        
        nums = []
        for i in se:
            nums.append(i)
        nums.sort()
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        if nums[0] == 0 and nums[1] == -1:
            return 2
        lef = 0
        rig = 1
        cnt = 1
        arr = []
        while rig < len(se):
            if nums[rig] - nums[lef] == cnt:
                rig +=1
                cnt+=1
            elif nums[rig] - nums[lef] != cnt:
                arr.append(cnt)
                rig+=1
                lef = rig-1
                cnt = 0
            arr.append(cnt)
        return max(arr)
        