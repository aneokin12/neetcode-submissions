from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Approach:
        Start by initializing graph as root, then traverse graph using
        DFS or BFS to define neighbor relationships
        '''
        # Define root
        if not node:
            return None
        
        mapped = {}
        mapped[node] = Node(node.val)
        dq = collections.deque([node])
        # bfs
        while dq:
            curr = dq.popleft()
            # how do we process a node?
            # TODO: do something with curr
            for n in curr.neighbors:
                if n not in mapped:
                    mapped[n] = Node(n.val)
                    dq.append(n)
                mapped[curr].neighbors.append(mapped[n])
        
        return mapped[node]
            



