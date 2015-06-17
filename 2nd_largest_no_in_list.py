# Enter your code here. Read input from STDIN. Print output to STDOUT
"""Problem Statement

Now, lets delve into one of the most basic data types in python, LIST. You are given 'n' numbers. Store them in a list and find the second largest number. Easy enough!

NOTE : Don't use insertion sort

Input Format

First line contains N. Second line contains Array A[] of N integers each separated by a space.

Output Format

Value of the second largest number.

Sample Input

5
2 3 6 6 5

Sample Output

5

Constraints
2 <= N <= 10
-100 <= A[i] <= 100
"""

N = input()
data = map(int, raw_input().split())
maxm = max(data)
temp = []
for i in data:
    if i != maxm:
        temp.append(i)
print max(temp)
