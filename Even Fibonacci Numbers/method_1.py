def fibonaci(x):
    if x == 0:
        return 0
    if x == 1 :
        return 1
    else: 
        return fibonaci(x-1) + fibonaci(x-2)

list = []
max = 4000000
i = 0
while True:
    if(fibonaci(i) > max):
        break
    elif fibonaci(i) %2 == 0:
        list.append(fibonaci(i))
    i+=1
        
print(sum(list))
