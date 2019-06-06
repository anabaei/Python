
def minSum(num, k):
  

    result = 0
    if (k==0):
        return result
    else:
        for j in range(0,k):
            num = sorted(num)
            print(num)
            number = num.pop()
            if (number == 1):
                num.append(number)
                break
            else:         
                num.append( int((number/2)+ (number % 2)))

        for i in num:
            result +=i   
        return result


print(minSum([2,66],4))