class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s
        print(len(t))
        s = s.replace(" ","")
        s = s.lower()
        l  = len(s) // 2
        arr = ["?","!","@","$"," ",",","'","."]
        for i in arr:

            if i in s:
                print("yes",i)
                s = s.replace(i,"")
        

        str = s
        l = len(str) // 2
        print(len(str))
        if len(str) % 2 != 0:
            s = str[:l]
            s2 = str[l+1:]
        else:
            s = str[:l]
            s2 = str[l:]
        
        print(s,s2)
        
        # str = "abba"
        # s = str[:2]
        # s2 = str[2:]
        
        # print(s,s2)
        
        if s == s2[::-1]:
            return True
        else:
            return False 


        