# 1
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

     # this method returns a readable anyobjest we have. It returns as string format our self.data
    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next"""
        self.next = new_next        

nodeA = SLLNode(1)
nodeA.next = SLLNode(2)
nodeA.next.next = SLLNode(3)


nodeB = SLLNode(4)
nodeB.next = SLLNode(5)
nodeB.next.next = SLLNode(9)

# nodeB = SLLNode(9)
# nodeB.set_next(nodeB)
# nodeB.set_data(1)
# print(nodeA.data)
# print(nodeB.data)

# def addNodes(nodeA, nodeB)


def addLinkLists(nodeA, nodeB):
    arrA=[]
    n = 0
    carryover= 0
    len = 1
  
    startNode = None
    while(nodeA or nodeB or carryover):
        carryover= 0
        n +=1
    
       
        vara = nodeA.data if nodeA else 0
        varb = nodeB.data if nodeB else 0
        varc = vara + varb
        nodeA = nodeA.next if nodeA else 0
        nodeB = nodeB.next if nodeB else 0
        if varc<10:
            varc 
        else: 
            varc = varc%10 
            carryover +=1
        if not startNode:
            newNode = startNode = SLLNode(varc)
          
        else:
            newNode.next = SLLNode(varc)
            newNode = newNode.next
        
      
    return startNode


print(addLinkLists(nodeA, nodeB))



## solution 2
class solution:
    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbersHelper(l1,l2,0)

    def addTwoNumbersHelper(self, l1,l2,c):
        data = l1.data + l2.data + c
        c = data/10
        data = SLLNode(data%10)

        # if l1 or l2 still have next then call helper recursivly

# call solution
# anwer = solution().addTwoNumbers(l1,l2)
# while anwer:
#     print(anwer.data)
#     anwer = anwer.next
