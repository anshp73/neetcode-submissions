class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i,e in enumerate(nums):
            diff = target - e
            if diff in d:
                return [d[diff],i]
            d[e] = i


        

            

        