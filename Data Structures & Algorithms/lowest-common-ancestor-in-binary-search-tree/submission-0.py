# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr_node):
            if not curr_node:
                return None
            # both values less, recurse to left subtree
            if curr_node.val > p.val and curr_node.val > q.val:
                return dfs(curr_node.left)
            # both values greater, recurse to right subtree
            elif curr_node.val < p.val and curr_node.val < q.val:
                return dfs(curr_node.right)
            # otherwise, curr_node is LCA
            else:
                return curr_node

        lca = dfs(root)
        return lca

        