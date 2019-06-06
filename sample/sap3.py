

array = [] 
n = int(input()) 
for i in range(0, n): 
    element = int(input()) 
    array.append(element)  

index = int(input())   
cnt = 0

for j,v in enumerate(array):    
    if(j < index and v > array[index]):
        cnt +=1
    elif(j > index and v < array[index]):
        cnt +=1
    else: continue    

print(cnt) 

    

       

