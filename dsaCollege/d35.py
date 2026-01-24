'''🟨 Question Title
Subarrays With Sum Less Than K

📝 Description
You are given an array arr consisting of non-negative integers and an integer K.
Return the number of contiguous subarrays whose sum of elements is strictly less than K.

📌 Example
Input
arr = [1, 2, 3]
K = 5

Output
4


💡 Explanation
Valid contiguous subarrays with sum less than 5 are:
[1] → 1
[2] → 2
[3] → 3
[1,2] → 3

Subarrays [2,3] and [1,2,3] exceed the limit.


✅ Public Test Cases
Test Case 1
 Input:
2 1 1
3

Output:
4


Test Case 2
 Input:
0 0 0
1

Output:
6


🔒 Private Test Cases
Test Case 1
 Input:
5 5 5
5

Output:
0


Test Case 2
 Input:
1
2

Output:
1


Test Case 3
 Input:
1 2 1 1
4

Output:
7


Test Case 4
 Input:
100
50

Output:
0


Test Case 5
 Input:
1 1 1 1
3

Output:
7


'''


'''🟨 Question Title
Longest Segment With At Most K Zeroes

📝 Description
You are given a binary array arr and an integer K.
Determine the maximum length of a contiguous segment that contains at most K zeroes.

📌 Example
Input
arr = [1, 1, 0, 0, 1, 1, 1]
K = 1

Output
4


💡 Explanation
The longest valid segment is:
[0, 1, 1, 1]

It contains only one zero and has length 4.

🧪 Test Cases
✅ Public Test Cases
Test Case 1
 Input:
0 0 1 1 1
2

Output:
5


Test Case 2
 Input:
1 1 1
0

Output:
3


🔒 Private Test Cases
Test Case 1
 Input:
0 0 0
1

Output:
1


Test Case 2
 Input:
1 0 1 0 1
2

Output:
5


Test Case 3
 Input:
1 1 0 1
0

Output:
2


Test Case 4
 Input:
0 1
1

Output:
2


Test Case 5
 Input:
1
0

Output:
1
'''

'''🟨 Question Title
Longest Substring With At Most K Distinct Alphabets

📝 Description
You are given a string s consisting of lowercase English alphabets and an integer K.
Return the maximum length of a contiguous substring that contains at most K distinct characters.

📌 Example
Input
s = "eceba"
K = 2

Output
3


💡 Explanation
The longest valid substring is:
"ece"

It contains only two distinct characters and has length 3.

🧪 Test Cases
✅ Public Test Cases
Test Case 1
 Input:
aa
1

Output:
2


Test Case 2
 Input:
abc
2

Output:
2


🔒 Private Test Cases
Test Case 1
 Input:
aabbcc
1

Output:
2


Test Case 2
 Input:
abcdef
3

Output:
3


Test Case 3
 Input:
a
1

Output:
1


Test Case 4
 Input:
abaccc
2

Output:
4


Test Case 5
 Input:
zzzz
1

Output:
4
'''

'''🟨 Question Title
Count Segments With Exactly K Odd Numbers

📝 Description
You are given an array arr of integers and an integer K.
Return the number of contiguous segments that contain exactly K odd numbers.

📌 Example
Input
arr = [1, 1, 2, 1, 1]
K = 3

Output
2


💡 Explanation
The valid contiguous segments are:
[1, 1, 2, 1]
[1, 2, 1, 1]

Each contains exactly three odd numbers.

✅ Public Test Cases
Test Case 1
 Input:
2 4 6
1

Output:
0


Test Case 2
 Input:
2 2 1 2 2
1

Output:
9


🔒 Private Test Cases
Test Case 1
 Input:
1 3 5
2

Output:
2


Test Case 2
 Input:
1
1

Output:
1


Test Case 3
 Input:
2 2 2
0

Output:
0


Test Case 4
 Input:
1 2 3 4 5
2

Output:
4


Test Case 5
 Input:
1 1 1 1
3

Output:
2


'''