#151
'''class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s= list(s)
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return " ".join(s)'''

#345
'''class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        v=set("AEIOUaieou")
        i=0
        j=len(s)-1
        while i<j:
            if s[i] not in v:
                i+=1
            elif s[j] not in v:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)'''