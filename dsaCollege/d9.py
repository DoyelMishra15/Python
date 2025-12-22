#list
a=[1,2,3,4,5]
x = [y for y in a if y%2==0]
print(x)

# tuple, set





#dictionary
#properties and declarations
#accessing dict elements
#dict methods

#1 leetcode
'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vi ={}
        for i in range(0,len(nums)):
            num = nums[i]
            need = target - num
            if need in vi:
                return(vi[need],i)
            vi[num]=i'''

'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for i in range(0,len(nums)):
            c = target - nums[i]
            if c in d:
                return(d[c],i)
            else:
                d[nums[i]]=i'''

#217 
'''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False'''

'''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d ={}
        for i in nums:
            if i in d:
                return True
            else:
                d[i]="heh"
        return False'''

#used in duplicates, 
# set operations like union, intersection, difference,only then use set