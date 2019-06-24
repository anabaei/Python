

import functools

#print(filter(lambda x: x>0, [4,2,1]))

def lambMap(arr):
    list(lambda x: print(x), arr)
    def f(x):
        print(len(x))

#        list(map(lambda x: x+x, arr))
#     list(map(lambda x: list(map(lambda y: y**2,x)) ,arr))
#     list(map(lambda x: print(list(map(lambda y: y**2 if y>0 else None ,x)))   , arr)) 
#    list(map(lambda x: print(list(map( lamda y:  ,x))) , arr)) 





print(lambMap([[1,-2,3],[2,3]]))