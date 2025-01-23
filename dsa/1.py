#Given an array with some integer type values. 
# Write a python script to sort array values

from array import *

arr = array('i',[45,3,6,86,32,5])
print("Original Array:", arr)
arr = array('i', sorted(arr))
print("Sorted array: ", arr)


#arr = [45,3,6,86,32,5]
#arr.sort()
#print("Sorted array: ", arr)