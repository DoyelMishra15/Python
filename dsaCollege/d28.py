#bubble sort
 
arr= [5,4,3,2,1]
'''for i in range(len(arr)-1,-1,-1):
  for j in range(i):
    if arr[j]>arr[j+1]:
      arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)'''

'''for i in range(len(arr)):
  for j in range(len(arr)-i-1):
    if arr[j]>arr[j+1]:
      arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)'''


for i in range(len(arr)-1):
  for j in range(1,len(arr)-i):
    if arr[j]<arr[j-1]:
      arr[j],arr[j-1]=arr[j-1],arr[j]
print(arr)


#905, did it myself, not of course

'''class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,-1,-1):
            for j in range(i):
                if arr[j]%2>arr[j+1]%2:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr'''
