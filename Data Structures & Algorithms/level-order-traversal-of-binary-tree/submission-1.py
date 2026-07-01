# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        store queue as List[tuple]: node.value and node's level
        initialize result as [[] * log(root.len)]
        when you pop queue, append queue.left and queue.right with one higher level than popped node
        append queue to res[level]
        return when queue is empty
        '''
        if not root:
            return []
        
        q: List[tuple] = [(root, 0)]
        res = {}

        while q:
            # curr = (node, output_index)
            node, output_index = q.pop(0)
            # add children to queue if they exist
            if node.left:
                q.append((node.left, output_index + 1))
            if node.right:
                q.append((node.right, output_index + 1))
            # set res[output_index] to [] if it doesn't exist
            res[output_index] = res.get(output_index, [])
            # at output_index, append node.val
            res[output_index].append(node.val)
        
        # return res.values()
        return list(res.values())

        