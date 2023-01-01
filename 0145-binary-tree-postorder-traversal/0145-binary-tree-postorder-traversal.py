class Solution:

	def postorderTraversal(self, root):

		if not root:

			return

		stack = [(root, False)]

		result = []

		while stack:

			node, toProcess = stack.pop()

			if not toProcess:

				stack.append((node, True))

				if node.right:

					stack.append((node.right, False))

				if node.left:

					stack.append((node.left, False))

			else:

				result.append(node.val)


		return result