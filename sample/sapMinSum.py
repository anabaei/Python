###
###    
###
def minSum(num, k):
    #result = 0 
    for j in range(0,k):
        result = 0
        maxindex=0
        max=-1
        for index, number in enumerate(num):
            result +=number   
            if(number>max):
                max=number
                maxindex=index
        if (max < 2):
            num[maxindex]= max
            break
        else:
            result = result - num[maxindex] 
            num[maxindex] = (round(max/2))
            result = result + round(max/2) 
    return result

print(minSum([100000,20,99999],10000000))
print(minSum([10,20,7],4))
print(minSum([10,20,99999],4))