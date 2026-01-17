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

#set 1

'''Question Title
Evaluate Reverse Polish Notation

Problem Description
You are given an array of strings tokens that represents an arithmetic expression in Reverse Polish Notation (RPN).
Evaluate the expression and return the result as an integer.
Rules:
Valid operators: +, -, *, /


Operands are 32-bit integers


Division truncates toward zero


Example: -9 / 2 = -4


The input expression is always valid


No division by zero



Constraints
4 <= tokens.length <= 10^4


tokens[i] is either:


a decimal integer (may start with -)


"+", "-", "*", "/"


All intermediate and final results fit in a 32-bit signed integer



Approach (Stack Intuition)
Keep a stack


If element is number → push onto stack


If element is operator → pop two numbers → compute → push result back


After all tokens → top of stack is the answer

Time Complexity: O(n)
 Space Complexity: O(n)

Example
Input
2 1 + 3 *

Output
9

Explanation
(2 + 1) * 3 = 9








Test Case
Input
Expected Output
1
2 1 + 3 *
9
2
4 13 5 / +
6
3
10 6 9 3 + -11 * / * 17 + 5 +
22
4
3 -4 *
-12
5
18
18
6
-9 2 /
-4
7
5 1 2 + 4 * + 5 -
14'''

#set3

'''Question Title
Stock Span Problem (Real-Time Stock Analysis)

Problem Description
You are given an integer array prices where prices[i] represents the stock price of a company on day i.
Return an array span such that:
 span[i] is the number of consecutive days (including today) the stock price has been less than or equal to today’s price.
This problem simulates a real-time stock trading system where traders want to know how strong today’s price is compared to previous days.
You must solve this problem using a stack that keeps track of indices in a monotonically decreasing order of stock prices.

Constraints
1 <= prices.length <= 10^5


1 <= prices[i] <= 10^5


Output array length must be the same as input



Example
Input
100 80 60 70 60 75 85

Output
[1, 1, 1, 2, 1, 4, 6]


Explanation
Day 0 (100) → span = 1


Day 1 (80) → lower than yesterday → span = 1


Day 2 (60) → lower → span = 1


Day 3 (70) → higher than 60 → span = 2


Day 4 (60) → lower → span = 1


Day 5 (75) → higher than 60, 70 → span = 4


Day 6 (85) → higher than 75, 80 → span = 6



Algorithm (Stack Intuition)
Keep a stack of indices


Stack stores previous prices in decreasing order


Go through prices from left to right


While current price ≥ top of stack → pop indices


If stack becomes empty → span = current index + 1


Else → span = distance from stack top


Push current index onto stack


Why Stack Works Here
Each price is pushed once and popped once


The stack always remembers the nearest greater element on the left


This avoids nested loops and makes it efficient for real-time systems



Complexity Analysis
Time Complexity: O(n)


Space Complexity: O(n)



Test Cases
Input
Expected Output
100 80 60 70 60 75 85
[1, 1, 1, 2, 1, 4, 6]
10 20 30 40
[1, 2, 3, 4]
40 30 20 10
[1, 1, 1, 1]
50
[1]
70 70 70
[1, 2, 3]


'''