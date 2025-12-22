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

#used in duplicates, 
# set operations like union, intersection, difference,only then use set