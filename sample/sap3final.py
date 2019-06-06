
def collision(speed,pos):

  
    cnt = 0
    for j,v in enumerate(speed):    
        if(j < pos and v > speed[pos]):
            cnt +=1
        elif(j > pos and v < speed[pos]):
            cnt +=1
        else: continue    

    return cnt

    

print(collision([8,3,6,3,2,2,4,8,1,6],7))      

