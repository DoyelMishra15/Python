#my set2
# 
'''Question Title
Daily Temperatures (Next Greater Element)

Problem Description
You are given an integer array temperatures where temperatures[i] represents the temperature on day i.
Return an array answer such that:
answer[i] is the number of days you have to wait after day i to get a warmer temperature.'''


'''If there is no future day with a warmer temperature, set answer[i] = 0.


You must solve this problem using a stack that keeps track of indices in a monotonically decreasing order of temperatures.

Constraints
1 <= temperatures.length <= 10^5


30 <= temperatures[i] <= 100


Output array length must be the same as input



Example
Input
73 74 75 71 69 72 76 73

Output
[1, 1, 4, 2, 1, 1, 0, 0]

Explanation
Day 0 (73) → wait 1 day for 74
Day 1 (74) → wait 1 day for 75
Day 2 (75) → wait 4 days for 76
Day 3 (71) → wait 2 days for 72
Day 4 (69) → wait 1 day for 72
Day 5 (72) → wait 1 day for 76
Day 6 → no warmer day → 0
Day 7 → no warmer day → 0


Algorithm (Stack Intuition)
Keep a stack of indices


Stack stores temperatures in decreasing order


Go through days left to right


While current temperature > top of stack → pop index


For popped index → days to wait = current index - popped index


Push current index onto stack


Remaining indices → no warmer day → answer = 0


Complexity Analysis
Time Complexity: O(n)


Space Complexity: O(n)



Test Case
Input
Expected Output
1
73 74 75 71 69 72 76 73
[1, 1, 4, 2, 1, 1, 0, 0]
2
30 40 50 60
[1, 1, 1, 0]
3
30 60 90
[1, 1, 0]
4
30 40 50 60 50 40 30
[1, 1, 1, 0, 0, 0, 0]
5
70 70 70
[0, 0, 0]
6
90
[0]
7
80 79 78 77
[0, 0, 0, 0]'''

