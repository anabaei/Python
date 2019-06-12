


array =[]

n = int(input()) 

for i in range(0,n):  

  lst=list(map(int,input().split()))
  array.append(lst)


for j in range(0,n):
    for k in array[j]:
        if (k > 0):
            print(k*k, end =" ")
    print("")




        
  


       

