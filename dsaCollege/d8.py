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