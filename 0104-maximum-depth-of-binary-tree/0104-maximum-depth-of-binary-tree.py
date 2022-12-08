class Solution:

	def maxDepth(self, root):

		resultDepth = 0

		if not root:

			return resultDepth

		stack = [(root, 1)]

		while stack:

			node, depth = stack.pop()

			if depth > resultDepth:

				resultDepth = depth

			if node.right:

				stack.append((node.right, depth+1))

			if node.left:

				stack.append((node.left, depth+1))

		return resultDepth