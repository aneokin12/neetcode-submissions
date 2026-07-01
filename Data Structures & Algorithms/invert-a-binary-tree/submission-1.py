# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        while q:
            node = q.pop(0)
            if node:     
                tmp = node.right
                node.right = node.left
                node.left = tmp
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

        