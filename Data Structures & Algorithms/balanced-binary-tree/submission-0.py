# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        heights = defaultdict(int)

        while stack:
            node = stack[-1]
            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_height = heights[node.left]
                right_height = heights[node.right]
                if abs(left_height - right_height) > 1:
                    return False
                heights[node] = 1 + max(left_height, right_height)
        return True