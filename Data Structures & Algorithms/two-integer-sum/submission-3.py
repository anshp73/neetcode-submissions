class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i,e in enumerate(nums):
            if target - e not in d:
                d[e] = i
            else:
                return [d[target-e],i]
        