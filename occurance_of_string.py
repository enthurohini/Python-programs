"""
"""

s = raw_input()
sub = raw_input()
f = 0
count = 0
for i in range(len(s)-len(sub)+1):
    if s[i] == sub[0]:
        for j in range(len(sub)):
            if s[i+j] != sub[j]:
                f = 1
                break
        if f == 0:
            count = count + 1  
           
print count
