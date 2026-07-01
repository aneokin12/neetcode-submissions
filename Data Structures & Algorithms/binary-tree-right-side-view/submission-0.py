# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        intuition:
        do a bfs, keeping track of the current level of the node
        if a node at res[level] exists, replace it with the current node
        else, increment the level and append it
        Time: O(n)
        Space: O(log(n))
        '''
        q = [(root, 0)]
        res = []
        
        while q:
            node, level = q.pop(0)
            if node:
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))
                # check for existence of res[level]: if len(res) - 1 less than level, it doesn't exist yet
                if level > len(res) - 1:
                    res.append(node.val)
                else:
                    res[level] = node.val
                print(res)
        return res

        