class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s
        print(len(t))
        s = s.replace(" ","")
        s = s.lower()
        l  = len(s) // 2
        arr = ["?","!","@","$"," ",",","'",".",":"]
        for i in arr:

            if i in s:
                print("yes",i)
                s = s.replace(i,"")
        

        i = 0
        j = len(s)-1
        bool = True
        while i < len(s) // 2 and j  > len(s) // 2:
            print(i,j)
            
            i+=1
            j-=1
            if s[i-1] != s[j+1]:
                bool = False
                break
        return bool


        