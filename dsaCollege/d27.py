#704

'''class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1'''

#374

'''# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while l<=r:
            m=(l+r)//2
            p=guess(m)
            if p==0:
                return m
            elif p==-1:
                r=m-1
            else:
                l=m+1'''

#278

'''# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m):
                r = m - 1          
            else:
                l = m + 1          
        return l'''