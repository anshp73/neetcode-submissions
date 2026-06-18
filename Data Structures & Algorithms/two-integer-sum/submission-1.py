class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in nums:
            if i not in d:
                if target-i  in nums:
                    d[i] = target-i
                    if i == target-i:
                        return [nums.index(i),nums.index(target-i)+1]
                    else:
                        return [nums.index(i),nums.index(target-i)]
                    break
        print(d)


            

        