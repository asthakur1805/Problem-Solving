class Solution:

	def preorderTraversal(self, root):

		if not root:

			return

		stack = [(root, False)]

		result = []

		while stack:

			node, toProcess = stack.pop()

			if not toProcess:

				if node.right:

					stack.append((node.right, False))

				if node.left:

					stack.append((node.left, False))

				stack.append((node, True))

			else:

				result.append(node.val)

		return result