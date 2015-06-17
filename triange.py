""" This code is to print traingle by making use of single loop and aingle print statements and arithematic operators. 
    Constraint 1 <= input value <= 9 """

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print i*(pow(10, (i-1))+ int(pow(10, (i-2))) + int(pow(10, (i-3))) + int(pow(10, (i-4))) + int(pow(10, (i-5))) + int(pow(10, (i-6))) + int(pow(10, (i-7))) + int(pow(10, (i-8))) + int(pow(10, (i-9))))

