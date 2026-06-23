# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverseTree(tree):
            if not tree:
                return False
            left = traverseTree(tree.left)
            right = traverseTree(tree.right)
            return f'#{tree.val} {left} {right}'
        return traverseTree(subRoot) in traverseTree(root)