
def lambdaMap(arr):

    # n = int(input()) 
    # for i in range(0,n):  
    #     lst=list(map(int,input().split()))
    #     arr.append(lst)

    
    for j in range(0,len(arr)):
        for k in arr[j]:
            if (k > 0):
                print(k*k, end =" ")
        print("")



lam = list(map(lambda x: map(lambda y: print(y**2) if y>0 else False, x) , [[2,-3,40,0],[333]] ))
    #lam =  lambda data, i, j: ((data[:,i]*data[:,j])**2 + 1)

#lambdaMap([[2,4,3,4],[4,-2,3]]) 
print(lam) 
        

  


       

