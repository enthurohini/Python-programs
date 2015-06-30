"""

Project Euler #87: Prime power triples


Problem Statement

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28=22+23+24
33=32+23+24
49=52+23+24
47=22+33+24

Given an integer N , Find out how many numbers less than or equal to N are there that can be expressed as a sum of a prime square , prime cube and prime fourth power.

Input Format
First line contains an integer T denoting the number of testcases.
The next T lines contain integer N.

Constraints
1≤T≤105
1≤N≤107

Output Format
The ith line containing the answer for the ith testcase.

Sample Input

1
50

Sample Output

4 


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()
N = input()
prime = [2,3]
def is_prime(N):
    for i in range(4,N):
        f = 0
        #print "i is " + str(i), f 
        for j in range(2,(i/2)+1):
            #print "j is " + str(j), f
            if i% j == 0:
                f = 1
                break
        if f == 0:
            prime.append(i)
    #print prime
            
is_prime(N)
count = 0
temp = [count+1 for i in prime for j in prime for k in prime if (i*i + j*j*j + k*k*k*k) <= N]
print len(temp)
