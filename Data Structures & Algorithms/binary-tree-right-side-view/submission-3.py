# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_nodes = []
        stack = deque([root])

        while stack:
            len_stack = len(stack)
            right_node = None
            print(stack)
            for i in range(len_stack):
                node = stack.popleft()
                if node and i == len_stack - 1:
                    right_node = node
                if node and node.left:
                    stack.append(node.left)
                if node and node.right:
                    stack.append(node.right)
            if right_node:
                right_nodes.append(right_node.val)
        return right_nodes
