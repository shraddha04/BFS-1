# Time Complexity : O(n) - number of nodes in tree
# Space Complexity : O(n) - n is number of nodes in tree
#                           for BFS - space is the for queue, for DFS - space is for the recursion stack
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""
BFS - traverse level by level and put nodes at next level into
the queue while popping out node at current level


DFS - Add a new list to the result when level == len(result),
else just append the node val to list at index level
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque


# BFS Solution
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)
            for i in range(0 ,size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels

# DFS Solution
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        self.result = []
        self.helper(root, 0, self.result)
        return self.result

    def helper(self, root, level, result):

        if root is None:
            return

        if len(result) == level:
            result.append([])

        result[level].append(root.val)

        self.helper(root.left, level +1, result)
        self.helper(root.right, level +1, result)







