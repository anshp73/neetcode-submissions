class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [ 1 for i in range(len(nums))]
        print(pre)

        pre[0] = nums[0]

        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i]
        
        print(pre)

        post = [1 for i in range(len(nums))]
        post[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i]
        print(post)
        fin = []
        for i in range(0,len(nums)):
            if i-1 < 0:
                pr = 1
                pos = post[i+1]
                fin.append(pr * pos)
            elif i + 1>= len(nums):
                pr = pre[i-1]
                pos = 1
                fin.append(pr * pos)
            else:
                pr = pre[i-1]
                pos = post[i+1]
                fin.append(pr * pos)
        print(fin)
        
        return fin
        
        