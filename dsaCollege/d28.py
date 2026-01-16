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


#875, H.W

#selection sort

arr= [5,3,4,2,1]
for i in range(len(arr)-1):
    min_i=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_i]:
            min_i=j
    arr[i],arr[min_i]=arr[min_i],arr[i]
print(arr)


#insertion sort

arr= [5,3,4,2,1]

n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
