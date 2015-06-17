# Enter your code here. Read input from STDIN. Print output to STDOUT
"""Problem Statement

Lets learn about list comprehensions!. You are given three integers X, Y and Z denoting the dimensions of a Cuboid. You have to print a list of all possible coordinates on the three dimensional grid, such that at any point the sum Xi + Yi + Zi is not equal to N. If X = 2, then possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

Input Format

Four integers X, Y, Z and N in four different lines.

Output Format

You have to print the list, in increasing order.

Sample Input

1
1
1
2

Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

"""

X = input()
Y = input()
Z = input()
N = input()

l1 = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k != N]
print l1
