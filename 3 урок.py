1)
n=[2, 3, 5, 9, 3]
l=len(n)
print("l = ", l)
print("n[0] = ", n[0])
 
chet=[]
nechet=[]
for i in range(l):
    if i%2==0:
        chet.append(n[i])
    else:
        nechet.append(n[i])
        
    sumOfElements = sum(nechet)    
        
print(chet, nechet)

print(sum(nechet))

2)
from functools import reduce
l = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x*y, l))


3)
my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)

4)
n = int(input())
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)