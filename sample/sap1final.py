
def minSum(num, km):
  
    result = 0  
    index=0
    maxindex=0
    maxvalue = num[0]

    for index, item in enumerate(num):
        if(item> maxvalue):
            maxvalue = item
            maxindex = index

     
    for indx, itm in enumerate(num):

        print(itm)  
             

  

minSum([10,20,7],4)
