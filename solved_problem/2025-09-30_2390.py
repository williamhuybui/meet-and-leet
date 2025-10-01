class Solution:
    def removeStars(self, s: str) -> str:
        #intialize stack as word type
        nstack: list = []

        #loop through s string
        for char in s:
            #check if char is *
            if char == '*': 
                #print("What it pop out",nstack.pop())
                nstack.pop() # yes then pop out last char in stack
            else:
                nstack.append(char) # no then add in stack

        #return a string    
        return ''.join(nstack)

        