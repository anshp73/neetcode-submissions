class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        
        def dict(str):
            d = {}

            for i in str:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] +=1
            return d
        arr = []
        b = []
        for i in strs:
            if dict(i) not in arr:
                arr.append(dict(i))
                b.append([i])
            else:
                index = arr.index(dict(i))
                b[index].append(i)
                

        print(arr,b)
            

        return b
            