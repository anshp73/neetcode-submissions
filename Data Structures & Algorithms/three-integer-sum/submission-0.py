class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        print(nums)
        arr = []
        for i in range(0,len(nums)-1):
            lef = i+1
            rig = len(nums) - 1
            while lef < rig:
                if nums[i] + nums[lef] + nums[rig] == 0:
                    arr.append([nums[i],nums[lef],nums[rig]])
                    break
                elif nums[i] + nums[lef] + nums[rig] < 0:
                    lef+=1
                else:
                    rig-=1
        return arr


        