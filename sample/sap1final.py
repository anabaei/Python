
def minSum(num, km):
  
    result = 0  
    index=0
    for j in range(0,km):
        print('j =',j)
        
        for k in num:
            if(num.index(k)==0):
                print('came here!')
                number= k
                index=0
            else:
                if(k>number):
                    number=k
                    index=num.index(k)
    
        if (number == 1):
            num[index]= number
            break
        else:         
            num[index] = int((number/2)+ (number % 2))
            #print('numer= ',number, 'index= ', index, 'num= ', num)
       
    for i in num:
        result +=i   
    return result

print(minSum([10,20,7],4))
