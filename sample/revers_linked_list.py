

## REVERSE A LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

     # this method returns a readable anyobjest we have. It returns as string format our self.data
    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):  
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next"""
        self.next = new_next        



node0 = SLLNode('0')
node1 = SLLNode('1')
node2 = SLLNode('2')
node3 = SLLNode('3')

node0.set_next(node1)
node1.set_next(node2)
node2.set_next(node3)

# node.get_next() 
# print(node2.get_next().data)
# current  current
# old prev  new next 
# old next  new prev   
# 1 -> 2 -> 3 -> 4 ->5

## Complexity
# Time O(N)
# Space O(1) : if we don't use a stack to save data and read through, if we do the it would be O(2N) or O(N) in space 
class Solution:
    def reverse(self, linkedlist):
        queue=[]
        newnode=None
        old_prev=None
        while(linkedlist.get_next()):
            old_next = linkedlist.get_next();
            current = linkedlist.data
            
            #create a new one
            if(old_next != None):
                newnode= SLLNode(old_next)
            newnode.set_next(current)

            queue.append(linkedlist.data)
            linkedlist = linkedlist.get_next()
        # node = SLLNode(linkedlist.data)
        # node0 = node
        print(newnode.get_next())
        
        # for i in range(len(queue)-1,-1,-1):
        #        newnode= SLLNode(queue[i]) 
        #        node.set_next(newnode)
        #        print(node.data)
        #        node = newnode            
        # return node0  

Solution().reverse(node0)



