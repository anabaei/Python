#cr2032

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

# print(minSum([100000,20,99999],10000000))
# print(minSum([10,20,7],4))
# print(minSum([10,20,99999],4))








# def cycle():
#     print("")
#     arr=["a","b","c","d","e"]
#     res=[]
#     for i,item in enumerate(arr):
#           res.append((i,item))
#           res.append("x")
#     for j in arr:
#         print(j)
#     print(res)



<<<<<<< HEAD
=======
# cycle()

>>>>>>> f6f1afe2519418539f82d9375ccd14c046c1a971
# def getMinimumMoves(arr):
   
#     cnt = 0
#     for i in (arr):
#         move = False
#         print('_____')
#         for j in range(arr.index(i), len(arr)):
#             print(arr[j])
#             if(i>arr[j]):
#                 move = True
#                 temp = i
#                 arr[arr.index(i)] = arr[j]
#                 arr[j] = temp
#         if(move):
#             cnt= cnt+1
#     return cnt 

    #print(cnt)
        
        
    
 
# [5,1,2,6,3]
#   [1,2,5,6,3]


#print(getMinimumMoves([5,1,3,2]))
 
# res=[]
# def myfunc(a):
#     if(a>0):
#         return res.append(a)



# def a():
#     map(lambda x: print(list(map(lambda y: y**2 if y>0 else print(""),x))),  [[2,4], [-1,3,4]])



# y = map(lambda x: res.append(x**2) if x>0 else None, (2, -3, 5))
# arr = [[1,2],[3,3]]
#y =  map(map(lambda x: res.append(x**2) if x>0 else None, (2, -3, 5)), arr)
#list(map(lambda x: print(list(map(lambda y: y**2 if y>0 else None ,x)))   , arr)) 
#a = [1,2,3,4]
#f = map( lambda x: print(list(map(lambda y: y**2 if y>0 else print(""),x))),

 # [[2,4], [-1,3,4]])
# print( a() )






def f(ar):
    if(ar>0):
        return (ar**2)



def lambMap(arr):
    #  list(map(lambda x: x+x, arr))
    #list(map(lambda x: list(map(lambda y: y**2,x)) ,arr))
    # list(map(lambda x: print(list(map(lambda y: y**2 if y>0 else None ,x)))   , arr)) 
 #   list(map(lambda x: print(list(map( lamda y:  ,x))) , arr)) 


#lambMap([[1,-2,3],[2,3]])


=======
# def lambMap(arr):
#     #  list(map(lambda x: x+x, arr))
#     #list(map(lambda x: list(map(lambda y: y**2,x)) ,arr))
#     #list(map(lambda x: print(list(map(lambda y: y**2 if y>0 else None ,x)))   , arr)) 
#     map(lambda x: print(x), arr)
    
>>>>>>> f6f1afe2519418539f82d9375ccd14c046c1a971


# import re

# def fun(s):
#     if( "@" not in s or "." not in s):
#         return False
#     com = s.split(".")    
#     username = s.split("@")
#     if (len(username) !=2 or len(com) != 2):
#         return False

  
#     website = com[0].split('@')
#     # print("/////////")
#     # print(website)
#     if(len(website) < 2):
#         return False
        

#     # print(website[1])
#     # print(bool(re.match('[a-zA-Z0-9]',website[1]))) 
#     # print("_________")

      

#     if( len(username[0]) == 0 or len(username[1]) ==0 or len(com[0]) == 0 or len(com[1]) ==0 or "." not in username[1] or len(com[1]) > 3 or bool(re.search('[!@#$%^&*(),.?":{}|<>]',website[1])) ):
#         return False 
    
#     if(len(website[1].split("_")) >1 or bool(re.search('[!@#$%^&*(),.?":{}|<>]',username[0]))):
#         return False
#     else:
       
#         return True


# def filter_mail(emails):
#     return list(filter(fun, emails))

# print(
# filter_mail([ 'brian-23@hackerrank.com','thatisit@thatisit', 'lara@hackerrank.com', 'britts_54@hackerrank.com'])
# )

# from functools import reduce

# xor = lambda x,y: (x+y)*2
# l = reduce(xor, [1,2,3,4])

# print(l)

    #arr.append(map(int, input().split()))
            
# lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
# lst.sort(key=lambda x:x[1])
# print(lst)



# def celsius(T):
#       return (float(5)/9)*(T-32)

# temperatures = (36.5, 37, 37.5, 38, 39)

# c = list(map(celsius,temperatures))
# f = list(map(lambda x: (float(5)/9)*(x-32),temperatures)) 

# print(f)


# # find primary numbers 
# import numpy 
# a = [[1,2,3],[10,20,30],[100,200,300]]

# b = [[1,2,3,4],[10,20,30,40],[100,200,300,400],[11,22,33,44]]

# cnt = 0
# #c = [[0,0,0],[0,0,0],[0,0,0]]

# def cal(b):
#     c = [[0,0,0]] * 3
#     final = [[0] * (len(b)-2)] * (len(b)-2)
#     print(final)
#     for index, result in enumerate(final):  
#         for j,k in enumerate(b):
#             col=0
#             c[j] = k
        
#     print(c)        
#     #for i,k in enumerate(final):
#         #print(i, k,'\n')
# cal(b)  


    

# ## This is the core of 3*3
# def co(a):
#      cnt = 0
#      sum=0
#      for i,data in enumerate(a):  
#          for j,k in enumerate(a[i]):
#              if(cnt==3 or cnt==5):
#                  cnt +=1
#                  continue
#              else:
#                  sum += k
#                  print(k, cnt)
#                  cnt +=1
#          print(sum)
#      return(sum)     

# #co(a)