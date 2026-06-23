# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        stack = deque([root])

        while stack:
            node = stack.popleft()
            if node:
                vals.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        vals.sort()
        return vals[k-1]