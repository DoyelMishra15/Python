##88
'''class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t=nums1[:]
        i,j,k=0,0,0
        while i<m and j<n:
            if t[i]<nums2[j]:
                nums1[k]=t[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        if i<m:
            while i<m:
                nums1[k]=t[i]
                i+=1
                k+=1
        else:
            while j<n:
                nums1[k]=nums2[j]
                j+=1
                k+=1'''
'''class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()'''

#643
'''class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        avg= s/k

        for i in range(k,len(nums)):
            s = s - nums[i-k] + nums[i]
            avg = max(avg, s/k)
        return avg'''
'''class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        avg= s/k
        for i in range(1, len(nums) - k + 1):
            s = s - nums[i-1] + nums[i+k-1]
            avg = max(avg, s/k)
        return avg'''


#1423

'''class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==len(cardPoints):
            return sum(cardPoints[:])
        else:
            lsum = sum(cardPoints[0:k])
            rsum, s=0,lsum
            for i in range(k-1,-1,-1):
                lsum = lsum - cardPoints[i]
                rsum= rsum + cardPoints[len(cardPoints) - k + i]
                s = max(s,lsum+rsum)
            return s'''



#1343
# class Solution:
#     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         count = 0
#         window_sum = sum(arr[:k])
#         target = k * threshold
#         if window_sum >= target:
#             count += 1
#         for i in range(k, len(arr)):
#             window_sum =window_sum + arr[i] - arr[i - k]
#             if window_sum >= target:
#                 count += 1
#         return count
