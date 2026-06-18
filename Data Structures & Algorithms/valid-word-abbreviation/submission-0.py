class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        lef = 0
        rig = 0
        bool  = True
        arr = ['0','1','2','3','4','5','6','7','8','9']
        while lef < len(word) and rig < len(abbr):
            print("start","arr",arr,"lef",lef,"word[lef]",word[lef],"rig",rig,"abbr[rig]",abbr[rig],"bool",bool )
            print("word",word,len(word),abbr)
            print("bool",len(word) == abbr)
            
            if word[lef] == abbr[rig]:
                lef += 1
                rig +=1
                # print("if equal","arr",arr,"lef",lef,"arr[lef]",arr[lef],"rig",rig,"arr[rig]",arr[rig],"bool",bool )
            else:
                if word[lef] != abbr[rig] and abbr[rig] not in arr :
                    print("not equal and rig is not an integer","arr",arr,"lef",lef,"word[lef]",word[lef],"rig",rig,"abbr[rig]",abbr[rig],"bool",bool )

                    bool = False
                    break
                elif word[lef] != abbr[rig] and abbr[rig]  in arr and rig + 1 < len(abbr):
                    print("not equal and rig is an integer","arr",arr,"lef",lef,"word[lef]",word[lef],"rig",rig,"abbr[rig]",abbr[rig],"bool",bool )

                    if abbr[rig+1] in arr:
                        lef = lef* (10) + (lef + 1) * 1
                    lef += rig
                    
                
                    
            

                print("over")
                lef+=1
                rig+=1
    
        print("bool",bool)

        return bool
                    



                    

        