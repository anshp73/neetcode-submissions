class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)

        for i in t:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        print(d2)
        if d == d2:
            return True
        else:
            return False
            
        

                