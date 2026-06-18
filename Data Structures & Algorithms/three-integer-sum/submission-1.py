class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        print(nums)
        
        arr = set()
        for i in range(0,len(nums)-1):
            lef = i+1
            rig = len(nums) - 1
            while lef < rig:
                if nums[i] + nums[lef] + nums[rig] == 0:

                    arr.add((nums[i],nums[lef],nums[rig]))
                    lef+=1
                    rig-=1
                elif nums[i] + nums[lef] + nums[rig] < 0:
                    lef+=1
                else:
                    rig-=1
        return [list(x) for x in arr]


        