class Solution:

	def maxDepth(self, root):

		if not root:

			return 0

		resultDepth = 0

		stack = [(root, 1)]

		while stack:

			node, depth = stack.pop()

			resultDepth = max(resultDepth, depth)

			if node.left:

				stack.append((node.left, depth+1))

			if node.right:

				stack.append((node.right, depth+1))


		return resultDepth