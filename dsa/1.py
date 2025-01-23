#Given an array with some integer type values. 
# Write a python script to sort array values

from array import *

arr = array('i',[45,3,6,86,32,5])
print("Original Array:", arr)
arr = array('i', sorted(arr))
print("Sorted array: ", arr)

print("Second Way: ")
arr1 = [45,3,6,86,32,5]
print("Original Array:", arr1)
arr1.sort()
print("Sorted array: ", arr)