arr = []

for i in range(0,14):
    if (i == 0): 
        result = 0
        arr.append(result)
        # print(result)
        continue
    elif (i == 1 or i ==2): 
        result = 1
        pre = 1
        arr.append(result)
        # print(result)
        continue
    else:
        temp = result
        result = result + pre
        pre = temp
        arr.append(result)
        # print(result)
print(arr)
   
