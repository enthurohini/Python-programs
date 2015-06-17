# Enter your code here. Read input from STDIN. Print output to STDOUT
"""You have to initialize your list L = [] and follow the N commands given in N lines.

Commands will be 1 of the 8 commands as given above, other than extend, and each command will have its value separated by space.

Follow this example: 
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]


NOTE: It can be done by using eval() function which can be used to evaluate string "insert". It will be more easy than checking whether it is print, pop or sort. It will simply evaluate that string.
"""


L = []
command = []
n = input()
for i in range(0,n):
    data = raw_input()
    data = data.split()
    command.append(data)
#print command
#print command[0]
#print command[0][1]
 
for j in range(0,len(command)):
    if len(command[j]) == 1 and command[j][0] == "print":
        print L
    elif len(command[j]) == 1 and command[j][0] == "sort":
        L.sort()
    elif len(command[j]) == 1 and command[j][0] == "pop":
        L.pop()
    elif len(command[j]) == 1 and command[j][0] == "reverse":
        L.reverse()
    elif len(command[j]) == 2 and command[j][0] == "append":
        L.append(int(command[j][1]))
    elif len(command[j]) == 2 and command[j][0] == "remove":
        L.remove(int(command[j][1]))
    elif len(command[j]) == 3:
        #a1 = int(command[j][1])
        #a2 = int(command[j[2]])
        #L.insert(a1,a2)
        a1 = int(command[j][1])
        a2 = int(command[j][2])
        L.insert(a1, a2)
        #print a1, a2
