class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        s1=""
        n=1
        for i in range(len(s)):
            print("i is ", i)
            for j in range(len(s1)):
                #print("j is ", j)
                #print("S1 before",s1)
                if s1[j]==s[i]:
                    if len(s1)>n:
                        n=len(s1)
                    s1=s1[j+1:]
                    #print("S1 after ",s1)
                    break
            
            s1+=s[i]
            #print("S1 after ",s1)
            #print(n,s1)
        if len(s1)>n:
            n=len(s1)
            
        return n
            