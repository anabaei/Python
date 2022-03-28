class Solution:
    def newfun():
        print("A")
        return None    

# Solution().newfun()

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

     # this method returns a readable anyobjest we have. It returns as string format our self.data
    def __repr__(self):
       res = str(self.data)
       while(node.next):
           node = node.next
           res = res + "-->" + str(node.data)
         
       print(res)
       return res

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

node = Node('apple')
node.get_data()
node.set_data(7)
node2 = Node(9)
node.set_next(node2)
# node.get_next() 
print(node.__repr__())


