#971

'''class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)'''


#680

'''class Solution:
    def validPalindrome(self, s: str) -> bool:
        s=list(s)
        i,j=0,len(s)-1
        t=0
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                t+=1
                if t > 1:
                    return False
                left = s[:i] + s[i+1:]
                right = s[:j] + s[j+1:]
                return left == left[::-1] or right == right[::-1]
        return True'''