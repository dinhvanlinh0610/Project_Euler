sum = 0
max = 4000000
c = 0
a = 0
b = 1
while c <= max:
    c = a + b
    a = b
    b = c
    
    if c % 2 == 0:
        sum +=c
    
print(sum)
