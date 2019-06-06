array = [] 
result = 0
n = int(input()) 
for i in range(0, n): 
    element = int(input()) 
    array.append(element)  
moves = int(input()) 


while(1):
    if(moves > 0):
       array = sorted(array)
       number = array.pop()
       array.append(round(number/2))
       moves -=1
    else: break

for i in array:
    result +=i

print(result)