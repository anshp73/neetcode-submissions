class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s
        print(len(t))
        s = s.replace(" ","")
        s = s.lower()
        l  = len(s) // 2
        arr = ["?","!","@","$"," "]
        for i in arr:

            if i in s:
                print("yes",i)
                s = s.replace(i,"")
        print("s",s,len(s))
        if len(s) % 2 == 0:
            print("here")
            s1 = s[:l]
            s2 = s[l:]
        else:
            print("ohere")
            s1 = s[:l-1]
            s2 = s[l:]

        
        print(s1,s2)
        print(len(s)//2)



        if s1 == s2[::-1]:
            return True
        else:
            return False


        