# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        need to do dfs here
        need to keep track of the current maximum seen when node is processed
        if node.val >= curr_max, increment result by 1
        '''
        res = 0
        def dfs(node, curr_max):
            nonlocal res
            if node:
                curr_max = max(node.val, curr_max)
                if node.val >= curr_max:
                    res += 1
                dfs(node.left, curr_max)
                dfs(node.right, curr_max)
        # run dfs with curr_max as root val
        dfs(root, root.val)
        return res

        