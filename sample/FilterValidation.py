import re

def fun(s):
    if( "@" not in s or "." not in s):
        return False
    com = s.split(".")    
    username = s.split("@")
    if (len(username) !=2 or len(com) != 2):
        return False

  
    website = com[0].split('@')
    # print("/////////")
    # print(website)
    if(len(website) < 2):
        return False
        

    # print(website[1])
    # print(bool(re.match('[a-zA-Z0-9]',website[1]))) 
    # print("_________")

      

    if( len(username[0]) == 0 or len(username[1]) ==0 or len(com[0]) == 0 or len(com[1]) ==0 or "." not in username[1] or len(com[1]) > 3 or bool(re.search('[!@#$%^&*(),.?":{}|<>]',website[1])) ):
        return False 
    
    if(len(website[1].split("_")) >1 or bool(re.search('[!@#$%^&*(),.?":{}|<>]',username[0]))):
        return False
    else:
       
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

print(
filter_mail([ 'brian-23@hackerrank.com','thatisit@thatisit', 'lara@hackerrank.com', 'britts_54@hackerrank.com'])
)
