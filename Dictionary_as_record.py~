""" There is a record of 'n' students, each record having name of student, percent marks obtained in Maths, Physics and Chemistry. Marks can be floating values. The user enters an integer 'n' followed by names and marks for the 'n' students. You are required to save the record in a dictionary data type. The user then enters name of a student and you are required to print the average percentage marks obtained by that student, correct to two decimal places. """


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
d = {}
for i in range(0, N):
    data = raw_input()
    data = data.split()
    d[data[0]] = [float(data[1]), float(data[2]), float(data[3])]
    
key = raw_input()
a = d[key]
print("%.2f" % ((a[0]+a[1]+a[2])/3))
