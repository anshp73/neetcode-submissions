class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {")":"(","]":"[","}":"{"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stk.append(i)
        
            else:
                if len(stk) == 0:
                    return False
                top = stk.pop()
            
                if top != d[i]:
                    return False
        if len(stk) == 0:
            return True
        else:
            return False
        