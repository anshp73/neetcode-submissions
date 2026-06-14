class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        
        

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    
        s = []

        for i in d:
            s.append((d[i],i))

        print(s)
        s.sort()
        ar = []
        print("here")
        for i in range(len(s)-1,-1,-1):
            print("helo")
            ar.append(s[i][1])
            print("Ar",ar)

        return ar[0:k]









        
            

        