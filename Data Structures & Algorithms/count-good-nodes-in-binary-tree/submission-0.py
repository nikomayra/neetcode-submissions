# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            good_paths = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            good_paths += dfs(node.left, maxVal)
            good_paths += dfs(node.right, maxVal)
            return good_paths
        return dfs(root, root.val)