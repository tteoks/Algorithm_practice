import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
import pprint
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solved by recursive inorder
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)
        
        return self.result

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val

            node = node.right
        
        return result

if __name__=="__main__":
	testcase = []
	print("hello world")

	sol = Solution()
	print(sol)
