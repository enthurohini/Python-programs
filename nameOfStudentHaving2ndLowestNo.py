# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Problem Statement

Now we will see how to implement a nested list. There is a classroom of 'n' students and you are given their names and marks in physics. Store them in a nested list and print the name of each student who got the second lowest marks in physics.

NOTE: If there are more than one student getting same marks, make sure you print the names of all students in alphabetical order, in different lines.

Input Format

Integer N followed by alternating sequence of N strings and N numbers.

Output Format

Name of student.

Constraints

    1≤N≤5

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output

Berry
Harry

"""

N = input()
data = []
for i in range(N):
    l1 = raw_input()
    l2 = float(raw_input())
    temp = [l1, l2]
    data.append(temp)
temp = []
for i in range(N):
    temp.append(data[i][1])
mini = min(temp)
T = []
for i in temp:
    if i != mini:
        T.append(i)
M = min(T)
name = [data[i][0] for i in range(len(data)) if data[i][1] == M]
name.sort()
for i in name:
    print i
