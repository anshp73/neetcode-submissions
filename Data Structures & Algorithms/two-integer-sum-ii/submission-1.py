class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lef = 0

        rig = len(numbers) - 1
        nums = numbers
        arr = []
        while (lef < rig):
            if nums[lef] + nums[rig] == target:
                
                arr.append(lef+1)
                arr.append(rig+1)
                break
            elif nums[lef] + nums[rig] > target:
                rig-=1
            else:
                lef += 1
        return arr
        
        