class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        l=[]
        d={}
        d1={}
        k=0
        for i in range(len(strs)):
            s=strs[i]
            
            l1=[]
            for j in range(len(s)):
                l1.append(s[j])
            l1.sort()
            if l1 not in d.values():
                d[i]=l1
                d1[i]=[s]
            else:
                for m,n in d.items():
                    if l1 == n:
                        d1[m].append(s)
            
            
        print(d)
        print(d1)
        for i in d1:
            l.append(d1[i])
        return l