# question: There are some courses pre requiest each other and user don't allow to take them on 
# the same semester, like course [1,0] course 1 has pre request 0. 

# use DFS. Depth-first search (DFS). 
# The algorithm starts at the root node and explores as far as possible along each branch before backtracking
# DFS is faster than BFS because BFS uses two operations on Queue  at each node visit.  although O(1) order, but still extra compare to DFS node visit

# DFS & BFS time complexity are O(V+E) vertices + edges
# DFS & BFS space complexity are hight of tree and number of nodes respectively
from pydoc import doc


class Solution:
    def __init__(self, arr):
        self.courses=[arr]
        self.valid={}
    def _hasCycle(self, tree, node, seen):
        if node in seen:
            return True
        if node not in tree:
            return False
        seen.add(node)
        for neihbours in tree[node]:
            if self._hasCycle(tree, neihbours, seen):
                return True
        return False
            
        
    def createTree(self):
        #create hash map
        for k in self.courses:
            for i,j in k:
                if i in self.valid:
                    self.valid[i].append(j)
                else:
                    self.valid[i] = [j]
        # for i in self.valid:
        for node in self.valid:
          if self._hasCycle(self.valid,node, set()):
              return False
        return True  


# 
res = Solution([[1,0], [2,1], [1,4],[4,2]])


print(res.createTree())

