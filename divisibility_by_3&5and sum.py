N1 = input("Enter number: ")
N2 = input("Enter number: ")
sum1 = 0
sum2 = 0
if N1<N2:
    for i in range(N1):
        if (i%3 == 0) or (i%5 == 0):
            sum1 = sum1 + i
    sum2 = sum1    
    for j in range(N1, N2):
        if (j%3 == 0) or (j%5 == 0):
            sum2 = sum2 + j
else:
    for i in range(N2):
        if (i%3 == 0) or (i%5 == 0):
            sum2 = sum2 + i
    sum1 = sum2    
    for j in range(N2, N1):
        if (j%3 == 0) or (j%5 == 0):
            sum1 = sum1 + j
        
print sum1
print sum2 
