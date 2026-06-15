class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        
        s = set(nums)
        x = []
        for i in s:
            x.append(i)
        
        lef = 0
        rig = 1
        cnt = 0
        while rig  < len(x):
            if x[rig] - x[lef] == 1:
                cnt+=1
                lef+=1
                rig+=1
            else:
                break
            
        return cnt+1
        